""" CogThiefGameToonSD: contains the catch game toon statedata. used by local and remote avatars """

from pandac.PandaModules import *
from toontown.toonbase.ToonBaseGlobal import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task.Task import Task


class CogThiefGameToonSD(StateData.StateData):
    """ CogThiefGameToonSD catching game char anim statedata """
    notify = DirectNotifyGlobal.directNotify.newCategory("CogThiefGameToonSD")

    FallBackAnim = 'slip-backward'
    FallFwdAnim = 'slip-forward'
    NeutralAnim = 'neutral'
    RunAnim = 'run'
    ThrowNeutralAnim = 'throw'
    ThrowRunAnim = 'throw'

    animList = [FallBackAnim, FallFwdAnim,
                NeutralAnim, RunAnim,
                ThrowNeutralAnim, ThrowRunAnim,
                ]

    def __init__(self, avId, game):
        self.avId = avId
        self.game = game
        self.isLocal = (avId == base.localAvatar.doId)
        self.toon = self.game.getAvatar(self.avId)
        self.unexpectedExit = False

        self.fsm = ClassicFSM.ClassicFSM(
            f'CogThiefGameAnimFSM-{self.avId}',
            [
                State.State('init',
                            self.enterInit,
                            self.exitInit,
                            ['normal']),
                State.State('normal',
                            self.enterNormal,
                            self.exitNormal,
                            ['throwPie', 'fallBack', 'fallForward']),
                # TODO: ClassicFSM does not allow transition from a state to the
                # same state. Separate throwPie into 2 states or fix ClassicFSM.
                State.State('throwPie',
                            self.enterThrowPie,
                            self.exitThrowPie,
                            ['normal', 'fallBack', 'fallForward', 'throwPie']),
                State.State('fallBack',
                            self.enterFallBack,
                            self.exitFallBack,
                            ['normal']),
                State.State('fallForward',
                            self.enterFallForward,
                            self.exitFallForward,
                            ['normal']),
                State.State('cleanup',
                            self.enterCleanup,
                            self.exitCleanup,
                            []),
            ],
            'init',
            'cleanup',
        )
        self.exitAlreadyCalled = False

    def load(self):
        self.setAnimState('off', 1.)
        # cache the animations
        for anim in self.animList:
            self.toon.pose(anim, 0)

    def unload(self):
        del self.fsm

    def enter(self):
        assert self.notify.debugStateCall(self)
        self.fsm.enterInitialState()

    def exit(self, unexpectedExit=False):
        assert self.notify.debugStateCall(self)
        if self.exitAlreadyCalled:
            return
        self.exitAlreadyCalled = True
        self.notify.debug(f'in exit self.toon.doId={self.toon.doId}')
        self.unexpectedExit = unexpectedExit
        self.fsm.requestFinalState()

    def enterInit(self):
        self.notify.debug('enterInit')
        self.toon.startBlink()
        self.toon.stopLookAround()
        if self.isLocal:
            self.game.initGameWalk()
        # force use of highest LOD
        self.toon.useLOD(1000)
        self.dropShadow = self.toon.dropShadow
        # fade out the drop shadow a bit
        self.origDropShadowColor = self.dropShadow.getColor()
        c = self.origDropShadowColor
        alpha = .35
        self.dropShadow.setColor(c[0], c[1], c[2], alpha)

    def exitInit(self):
        pass

    def setAnimState(self, newState, playRate):
        """Safe change the anim state of the toon."""
        if not self.unexpectedExit:
            # we do this to stop an animFSM state in flux error
            self.toon.setAnimState(newState, playRate)

    def enterNormal(self):
        self.notify.debug('enterNormal')
        self.setAnimState('CogThiefRunning', 1.)
        if self.isLocal:
            self.game.startGameWalk()
        self.toon.lerpLookAt(Vec3.forward() + Vec3.up(), time=.2, blink=0)

    def exitNormal(self):
        self.notify.debug('exitNormal')
        self.setAnimState('off', 1.)
        if self.isLocal:
            self.game.stopGameWalk()
        self.toon.lerpLookAt(Vec3.forward(), time=.2, blink=0)

    def throwPie(self, pieModel, handNode):
        """ this is a nasty little hack to work around the fact
        that FSMs will not exit/re-enter a state if you try to
        transition to the current state.
        """
        if self.fsm.getCurrentState().getName() == 'throwPie':
            self.fsm.request('normal')
        self.fsm.request('throwPie', [pieModel, handNode])

    def enterThrowPie(self, pieModel, handNode):
        """ pie model is placed under handNode in this state;
        this function takes ownership of the pie model """
        self.notify.debug('enterThrowPie')
        self.setAnimState('CatchEating', 1.)
        if self.isLocal:
            self.game.startGameWalk()

        self.pieModel = pieModel
        # make sure the scale stays the same wrt render
        renderScale = pieModel.getScale(render)
        pieModel.reparentTo(handNode)
        pieModel.setScale(render, renderScale)

        # transition to 'normal' after one anim cycle
        def finishedEating(self=self, pieModel=pieModel):
            self.fsm.request('normal')
            return Task.done

        duration = self.toon.getDuration('catch-eatneutral')
        self.eatIval = Sequence(
            Parallel(WaitInterval(duration),
                     # toon throw the pie halfway through animation
                     Sequence(LerpScaleInterval(pieModel, duration / 2.,
                                                pieModel.getScale() * .5,
                                                blendType='easeInOut'),
                              Func(pieModel.hide),
                              ),
                     ),
            Func(finishedEating),
            name=self.toon.uniqueName('eatingIval')
        )
        self.eatIval.start()

    def exitThrowPie(self):
        # if we were to 'finish' the ival, we could run into trouble with
        # nested 'request' calls
        self.eatIval.pause()
        del self.eatIval

        self.pieModel.reparentTo(hidden)
        self.pieModel.removeNode()
        del self.pieModel

        self.setAnimState('off', 1.)
        if self.isLocal:
            self.game.stopGameWalk()

    def enterFallBack(self):
        self.notify.debug('enterFallBack')

        if self.isLocal:
            # play 'oof'
            base.playSfx(self.game.sndOof)

        duration = 1.
        animName = self.FallBackAnim
        startFrame = 12
        totalFrames = self.toon.getNumFrames(animName)
        frames = (totalFrames - 1) - startFrame
        frameRate = self.toon.getFrameRate(animName)
        newRate = frames / duration
        playRate = newRate / frameRate

        def resume(self=self):
            self.fsm.request('normal')

        self.fallBackIval = Sequence(
            ActorInterval(self.toon, animName, startTime=startFrame / newRate,
                          endTime=totalFrames / newRate, playRate=playRate),
            FunctionInterval(resume),
        )

        self.fallBackIval.start()

    def exitFallBack(self):
        # don't 'stop/finish' the stunnedIval; it will attempt to
        # transition to 'normal', when we're already in the process
        # of transitioning somewhere
        self.fallBackIval.pause()
        del self.fallBackIval

    def enterFallForward(self):
        self.notify.debug('enterFallForward')

        if self.isLocal:
            # play 'oof'
            base.playSfx(self.game.sndOof)

        duration = 1.
        animName = self.FallFwdAnim
        startFrame = 12
        totalFrames = self.toon.getNumFrames(animName)
        frames = (totalFrames - 1) - startFrame
        frameRate = self.toon.getFrameRate(animName)
        newRate = frames / duration
        playRate = newRate / frameRate

        def resume(self=self):
            self.fsm.request('normal')

        self.fallFwdIval = Sequence(
            ActorInterval(self.toon, animName, startTime=startFrame / newRate,
                          endTime=totalFrames / newRate, playRate=playRate),
            FunctionInterval(resume),
        )

        self.fallFwdIval.start()

    def exitFallForward(self):
        # don't 'stop/finish' the stunnedIval; it will attempt to
        # transition to 'normal', when we're already in the process
        # of transitioning somewhere
        self.fallFwdIval.pause()
        del self.fallFwdIval

    def enterCleanup(self):
        self.notify.debug(f'enterCleanup {self.toon.doId}')
        if self.toon and not self.toon.isEmpty():
            self.toon.stopBlink()
            self.toon.startLookAround()
            if self.isLocal:
                self.game.stopGameWalk()
                self.game.destroyGameWalk()
            # restore the LODs
            self.toon.resetLOD()
            self.dropShadow.setColor(self.origDropShadowColor)

    def exitCleanup(self):
        pass
