from . import DistributedSuitInterior
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State

from toontown.toonbase import ToontownGlobals
class DistributedEndlessSuitInterior(DistributedSuitInterior.DistributedSuitInterior):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedSuitInterior')

    def __init__(self, cr):
        DistributedSuitInterior.DistributedSuitInterior.__init__(self, cr)
        self.fsm = ClassicFSM.ClassicFSM('DistributedEndlessSuitInterior',
                                         [State.State('WaitForAllToonsInside',
                                                      self.enterWaitForAllToonsInside,
                                                      self.exitWaitForAllToonsInside,
                                                      ['Elevator']),
                                          State.State('Elevator',
                                                      self.enterElevator,
                                                      self.exitElevator,
                                                      ['Battle']),
                                          State.State('Battle',
                                                      self.enterBattle,
                                                      self.exitBattle,
                                                      ['Resting',
                                                       'Reward',
                                                       'ReservesJoining']),
                                          State.State('ReservesJoining',
                                                      self.enterReservesJoining,
                                                      self.exitReservesJoining,
                                                      ['Battle']),
                                          State.State('Resting',
                                                      self.enterResting,
                                                      self.exitResting,
                                                      ['Elevator']),
                                          State.State('Reward',
                                                      self.enterReward,
                                                      self.exitReward,
                                                      ['Off']),
                                          State.State('Off',
                                                      self.enterOff,
                                                      self.exitOff,
                                                      ['Elevator',
                                                       'WaitForAllToonsInside',
                                                       'Battle']),
                                          ],
                                         # Initial State
                                         'Off',
                                         # Final State
                                         'Off',
                                         )

        # make sure we're in the initial state
        self.fsm.enterInitialState()

    def __uniqueName(self, name):
        DistributedEndlessSuitInterior.id += 1
        return name + f'{DistributedEndlessSuitInterior.id}'


    def generate(self):
        """generate(self)
        This method is called when the DistributedObject is reintroduced
        to the world, either for the first time or from the cache.
        """
        assert(self.notify.debug("generate()"))
        DistributedObject.DistributedObject.generate(self)

        # listen for the generate event, which will be thrown after the
        # required fields are filled in
        self.announceGenerateName = self.uniqueName('generate')
        self.accept(self.announceGenerateName, self.handleAnnounceGenerate)

        # Load the elevator model
        self.elevatorModelIn = loader.loadModel(
                                'phase_4/models/modules/elevator')
        self.leftDoorIn = self.elevatorModelIn.find('**/left-door')
        self.rightDoorIn = self.elevatorModelIn.find('**/right-door')

        self.elevatorModelOut = loader.loadModel(
                                'phase_4/models/modules/elevator')
        self.leftDoorOut = self.elevatorModelOut.find('**/left-door')
        self.rightDoorOut = self.elevatorModelOut.find('**/right-door')

    def setElevatorLights(self, elevatorModel):
        # we don't want elevator lights for endless buildings
        return

    def __playElevator(self, ts, name, callback):
        # Load the floor model

        SuitHs = []  # Heading angles
        SuitPositions = []

        if self.floorModel:
            self.floorModel.removeNode()

        if (self.currentFloor == 0):
            # bottom floor
            self.floorModel = loader.loadModel('phase_7/models/modules/suit_interior')
            SuitHs = self.BottomFloor_SuitHs
            SuitPositions = self.BottomFloor_SuitPositions
        elif (self.currentFloor == (self.currentFloor % 4 == 0)):
            # Boss floor
            self.floorModel = loader.loadModel('phase_7/models/modules/boss_suit_office')
            SuitHs = self.BossOffice_SuitHs
            SuitPositions = self.BossOffice_SuitPositions
        else:
            # middle floor
            self.floorModel = loader.loadModel('phase_7/models/modules/cubicle_room')
            SuitHs = self.Cubicle_SuitHs
            SuitPositions = self.Cubicle_SuitPositions

        self.floorModel.reparentTo(render)

        # We need to name this something more useful (and we'll need the
        # location of the opposite elevator as well)
        elevIn = self.floorModel.find('**/elevator-in')
        elevOut = self.floorModel.find('**/elevator-out')

        # Position the suits

        for index in range(len(self.suits)):
            assert (self.notify.debug('setting suit: %d to pos: %s' % \
                                      (self.suits[index].doId, SuitPositions[index])))
            self.suits[index].setPos(SuitPositions[index])
            if (len(self.suits) > 2):
                self.suits[index].setH(SuitHs[index])
            else:
                self.suits[index].setH(
                    170)  # if there's 2 or 1 suits, make them face fwd since there's no other suits they would be to be talking to
            self.suits[index].loop('neutral')

        # Position the toons
        for toon in self.toons:
            toon.reparentTo(self.elevatorModelIn)
            assert (self.toonIds.count(toon.doId) == 1)
            index = self.toonIds.index(toon.doId)
            assert (index >= 0 and index <= 3)
            toon.setPos(ElevatorPoints[index][0],
                        ElevatorPoints[index][1],
                        ElevatorPoints[index][2])
            toon.setHpr(180, 0, 0)
            toon.loop('neutral')

        # Show the elevator and position it in the correct place for the floor
        self.elevatorModelIn.reparentTo(elevIn)
        # Start with the doors in closed position
        self.leftDoorIn.setPos(3.5, 0, 0)
        self.rightDoorIn.setPos(-3.5, 0, 0)

        # Show the elevator and position it in the correct place for the floor
        self.elevatorModelOut.reparentTo(elevOut)
        # Start with the doors in closed position
        self.leftDoorOut.setPos(3.5, 0, 0)
        self.rightDoorOut.setPos(-3.5, 0, 0)

        # Position the camera behind the toons
        camera.reparentTo(self.elevatorModelIn)
        camera.setH(180)
        camera.setPos(0, 14, 4)

        # Play elevator music
        base.playMusic(self.elevatorMusic, looping=1, volume=0.8)

        # Ride the elevator, then open the doors.
        track = Sequence(
            ElevatorUtils.getRideElevatorInterval(ELEVATOR_NORMAL),
            ElevatorUtils.getOpenInterval(self, self.leftDoorIn, self.rightDoorIn,
                                          self.openSfx, None, type=ELEVATOR_NORMAL),
            Func(camera.wrtReparentTo, render),
        )

        for toon in self.toons:
            track.append(Func(toon.wrtReparentTo, render))
        track.append(Func(callback))
        track.start(ts)
        self.activeIntervals[name] = track

    def enterElevator(self, ts=0):
        # Load model for the current floor and the suit models for the floor
        assert (self.notify.debug('enterElevator()'))

        self.currentFloor += 1
        self.cr.playGame.getPlace().currentFloor = self.currentFloor
        self.setElevatorLights(self.elevatorModelIn)
        self.setElevatorLights(self.elevatorModelOut)

        self.__playElevator(ts, self.elevatorName, self.__handleElevatorDone)

        # Get the floor multiplier a constant 6x value
        mult = ToontownBattleGlobals.getCreditMultiplier(6)
        # Now set the inventory battleCreditMult
        base.localAvatar.inventory.setBattleCreditMultiplier(mult)

    def __addToon(self, toon):
        assert(self.notify.debug('addToon(%d)' % toon.doId))
        self.accept(toon.uniqueName('disable'),
                        self.__handleUnexpectedExit, extraArgs=[toon])

    def __handleUnexpectedExit(self, toon):
        self.notify.warning('handleUnexpectedExit() - toon: %d' % toon.doId)

        self.__removeToon(toon, unexpected=1)

    def __removeToon(self, toon, unexpected=0):
        # Reward the toon for their efforts based on last checkpoint
        self.rewardToonBasedOnCheckpoint(toon)
        if (self.toons.count(toon) == 1):
            self.toons.remove(toon)
        self.ignore(toon.uniqueName('disable'))

    def rewardToonBasedOnCheckpoint(self, toon):
        #TODO write logic for this

        # Reward gag experience and whatnot

        return

    def enterReward(self, ts=0):
        assert(self.notify.debug('enterReward()'))
        base.localAvatar.b_setParent(ToontownGlobals.SPHidden)
        request = {
            "loader": ZoneUtil.getBranchLoaderName(self.extZoneId),
            "where": ZoneUtil.getToonWhereName(self.extZoneId),
            "how": "elevatorIn",
            "hoodId": ZoneUtil.getHoodId(self.extZoneId),
            "zoneId": self.extZoneId,
            "shardId": None,
            "avId": -1,
            "bldgDoId": self.distBldgDoId
            }
        # Presumably, suitInterior.py has hung a hook waiting for
        # this request. I mimicked what DistributedDoor was doing.
        messenger.send("DSIDoneEvent", [request])
        return None

    def exitReward(self):
        return None