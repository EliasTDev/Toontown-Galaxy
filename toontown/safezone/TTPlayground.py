import random

from direct.fsm import ClassicFSM, State
from direct.task.Task import Task
from panda3d.core import *
from toontown.building import Elevator
from toontown.hood import ZoneUtil
from toontown.launcher import DownloadForceAcknowledge
from toontown.toonbase import ToontownGlobals

from . import Playground


class TTPlayground(Playground.Playground):
    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = "elevatorDone"

    def load(self):
        """"
        self.fsm = ClassicFSM.ClassicFSM('TTPlayground',
                                         [State.State('start',
                                                      self.enterStart,
                                                      self.exitStart,
                                                      ['walk', 'tunnelIn', 'teleportIn',
                                                       'doorIn',
                                                       ]),
                                             State.State('walk',
                                                         self.enterWalk,
                                                         self.exitWalk,
                                                         ['stickerBook', 'teleportOut',
                                                          'tunnelOut', 'DFA', 'doorOut',
                                                          'elevator', 'stopped',
                                                          ]),
                                             State.State('stopped',
                                                         self.enterStopped,
                                                         self.exitStopped,
                                                         ['walk', 'teleportOut', 'elevator'
                                                          ]),
                                             State.State('stickerBook',
                                                         self.enterStickerBook,
                                                         self.exitStickerBook,
                                                         ['walk', 'DFA',
                                                          'elevator',
                                                          ]),


                                             # Download Force Acknowlege:
                                             State.State('DFA',
                                                         self.enterDFA,
                                                         self.exitDFA,
                                                         ['DFAReject', 'teleportOut', 'tunnelOut']),
                                             State.State('DFAReject',
                                                         self.enterDFAReject,
                                                         self.exitDFAReject,
                                                         ['walk']),
                                             State.State('teleportIn',
                                                         self.enterTeleportIn,
                                                         self.exitTeleportIn,
                                                         ['walk',
                                                          ]),
                                             State.State('teleportOut',
                                                         self.enterTeleportOut,
                                                         self.exitTeleportOut,
                                                         ['teleportIn', 'final'
                                                          ]),
                                             State.State('doorIn',
                                                         self.enterDoorIn,
                                                         self.exitDoorIn,
                                                         ['walk']),
                                             State.State('doorOut',
                                                         self.enterDoorOut,
                                                         self.exitDoorOut,
                                                         ['walk']),

                                             State.State('tunnelIn',
                                                         self.enterTunnelIn,
                                                         self.exitTunnelIn,
                                                         ['walk']),
                                             State.State('tunnelOut',
                                                         self.enterTunnelOut,
                                                         self.exitTunnelOut,
                                                         ['final']),
                                             State.State('elevator',
                                                         self.enterElevator,
                                                         self.exitElevator,
                                                         ['walk', 'stopped']),
                                             State.State('final',
                                                         self.enterFinal,
                                                         self.exitFinal,
                                                         ['start'])],
                                         # Initial State
                                         'start',
                                         # Final State
                                         'final',
                                         )
        self.parentFSM.getStateNamed("TTPlayground").addChild(self.fsm)
        """
        Playground.Playground.load(self)

    def unload(self):
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        taskMgr.doMethodLater(1, self.__birds, 'TT-birds')

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('TT-birds')

    def __birds(self, task):
        base.playSfx(random.choice(self.loader.birdSound))
        t = (random.random() * 20.0) + 1
        taskMgr.doMethodLater(t, self.__birds, 'TT-birds')
        return Task.done

    def doRequestLeave(self, requestStatus):
        # when it's time to leave, check their trialer status first
        self.fsm.request('trialerFA', [requestStatus])

    def enterDFA(self, requestStatus):
        """
        Override the base class because here we specifically ask for
        phase 5, the toontown central streets.
        - NEW: we can now go home.  Check the hood before assuming we
        are going to the streets
        """
        doneEvent = "dfaDoneEvent"
        self.accept(doneEvent, self.enterDFACallback, [requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        hood = ZoneUtil.getCanonicalZoneId(requestStatus['hoodId'])
        if hood == ToontownGlobals.MyEstate:
            # Ask if we can enter phase 5.5
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(
                ToontownGlobals.MyEstate))
        elif hood == ToontownGlobals.GoofySpeedway:
            # Ask if we can enter phase 6
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(
                ToontownGlobals.GoofySpeedway))
        elif hood == ToontownGlobals.PartyHood:
            # ask if we can enter phase 13
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(
                ToontownGlobals.PartyHood))
        else:
            # Ask if we can enter phase 5
            self.dfa.enter(5)

    def showPaths(self):
        # Overridden from Playground to fill in the correct parameters
        # for showPathPoints().
        from toontown.classicchars import CCharPaths
        from toontown.toonbase import TTLocalizer
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Mickey))

    # elevator state
    # (For boarding a building elevator)

    def enterElevator(self, distElevator, skipDFABoard=0):
        assert(self.notify.debug("enterElevator()"))

        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed("elevator"),
                                          self.elevatorDoneEvent,
                                          distElevator)
        if skipDFABoard:
            self.elevator.skipDFABoard = 1
        # elevatorFSM is now on the DO
        distElevator.elevatorFSM = self.elevator
        self.elevator.load()
        self.elevator.enter()

    def exitElevator(self):
        assert(self.notify.debug("exitElevator()"))
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator

    def detectedElevatorCollision(self, distElevator):
        self.notify.debug("detectedElevatorCollision()")
        self.fsm.request("elevator", [distElevator])

    def handleElevatorDone(self, doneStatus):
        self.notify.debug("handling elevator done event")
        where = doneStatus['where']
        if (where == 'reject'):
            # If there has been a reject the Elevator should show an
            # elevatorNotifier message and put the toon in the stopped state.
            # Don't request the walk state here. Let the the toon be stuck in the
            # stopped state till the player removes that message from his screen.
            # Removing the message will automatically put him in the walk state there.
            # Put the player in the walk state only if there is no elevator message.
            if hasattr(base.localAvatar, "elevatorNotifier") and base.localAvatar.elevatorNotifier.isNotifierOpen():
                pass
            else:
                self.fsm.request("walk")
        elif (where == 'exit'):
            self.fsm.request("walk")
        elif (where == 'TTPlayground'):
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
       
        else:
            self.notify.error("Unknown mode: " + where +
                              " in handleElevatorDone")
