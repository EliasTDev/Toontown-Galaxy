""" DistributedAnimatedProp module: contains the DistributedAnimatedProp
    class, the client side representation of a 'landmark door'."""

from pandac.PandaModules import *
from direct.distributed.ClockDelta import *

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.distributed import DistributedObject


class DistributedAnimatedProp(DistributedObject.DistributedObject):
    """
    DistributedAnimatedProp class:  The client side representation of any
    simple animated prop.
    """

    def __init__(self, cr):
        """constructor for the DistributedAnimatedProp"""
        DistributedObject.DistributedObject.__init__(self, cr)
        # ("__init()")

        self.fsm = ClassicFSM.ClassicFSM('DistributedAnimatedProp',
                                         [State.State('off',
                                                      self.enterOff,
                                                      self.exitOff,
                                                      ['playing',
                                                       'attract']),
                                             State.State('attract',
                                                         self.enterAttract,
                                                         self.exitAttract,
                                                         ['playing']),
                                             State.State('playing',
                                                         self.enterPlaying,
                                                         self.exitPlaying,
                                                         ['attract'])],
                                         # Initial State
                                         'off',
                                         # Final State
                                         'off',
                                         )
        self.fsm.enterInitialState()
        # self.generate will be called automatically.

    def generate(self):
        """
        This method is called when the DistributedObject is reintroduced
        to the world, either for the first time or from the cache.
        """
        # ("generate()")
        DistributedObject.DistributedObject.generate(self)

    def announceGenerate(self):
        """
        This method is called when the DistributedObject is reintroduced
        to the world, either for the first time or from the cache.
        """
        # ("announceGenerate()")
        DistributedObject.DistributedObject.announceGenerate(self)
        self.setState(self.initialState, self.initialStateTimestamp)
        del self.initialState
        del self.initialStateTimestamp

    def disable(self):
        # ("disable()")
        # Go to the off state when the object is put in the cache
        self.fsm.request("off")
        DistributedObject.DistributedObject.disable(self)
        # self.delete() will automatically be called.

    def delete(self):
        # ("delete()")
        del self.fsm
        DistributedObject.DistributedObject.delete(self)

    def setPropId(self, propId):
        """
        required dc field.
        """
        # ("setPropId(%s)"%(propId,))
        assert "propId" not in self.__dict__
        self.propId = propId

    def setAvatarInteract(self, avatarId):
        """
        required dc field.
        """
        # ("setAvatarInteract(%s)"%(avatarId,))
        assert avatarId not in self.__dict__
        self.avatarId = avatarId

    def setOwnerDoId(self, ownerDoId):
        """
        required dc field.
        """
        # ("setOwnerDoId(%s)"%(ownerDoId,))
        assert "ownerDoId" not in self.__dict__
        self.ownerDoId = ownerDoId

    def setState(self, state, timestamp):
        """
        required dc field.
        """
        #("setState(%s, %d)" % (state, timestamp))
        if self.isGenerated():
            self.fsm.request(
                state, [
                    globalClockDelta.localElapsedTime(timestamp)])
        else:
            self.initialState = state
            self.initialStateTimestamp = timestamp

    # def __getPropNodePath(self):
    #    #("__getPropNodePath()")
    #    if (not self.__dict__.has_key('propNodePath')):
    #        self.propNodePath=self.cr.playGame.hood.loader.geom.find(
    #                "**/prop"+self.propID+":*_DNARoot")
    #    return self.propNodePath

    def enterTrigger(self, args=None):
        # ("enterTrigger(args="+str(args)+")")
        messenger.send("DistributedAnimatedProp_enterTrigger")
        self.sendUpdate("requestInteract")
        # the AI server will reply with toonInteract or rejectInteract.

    def exitTrigger(self, args=None):
        # ("exitTrigger(args="+str(args)+")")
        messenger.send("DistributedAnimatedProp_exitTrigger")
        self.sendUpdate("requestExit")
        # the AI server will reply with avatarExit.

    def rejectInteract(self):
        """Server doesn't let the avatar interact with prop"""
        # ("rejectInteract()")
        self.cr.playGame.getPlace().setState('walk')

    def avatarExit(self, avatarId):
        return
        # ("avatarExit(avatarId=%s)"%(avatarId,))

    ##### off state #####

    def enterOff(self):
        return
        # ("enterOff()")

    def exitOff(self):
        return
        # ("exitOff()")

    ##### attract state #####

    def enterAttract(self, ts):
        return
        # ("enterAttract()")

    def exitAttract(self):
        return
        # ("exitAttract()")

    ##### playing state #####

    def enterPlaying(self, ts):
        return
        # ("enterPlaying()")

    def exitPlaying(self):
        return
        # ("exitPlaying()")
