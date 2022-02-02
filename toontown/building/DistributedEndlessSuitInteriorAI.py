from . import DistributedSuitInteriorAI
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import DistributedBattleBldgAI

class DistributedEndlessSuitInteriorAI(DistributedSuitInteriorAI.DistributedSuitInteriorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEndlessSuitInteriorAI')

    def __init__(self, air, elevator):
        self.air = air
        DistributedSuitInteriorAI.DistributedSuitInteriorAI.__init__(self, air, elevator)
        self.numFloors = float('inf')
        self.extZoneId, self.zoneId = elevator.bldg.getExteriorAndInteriorZoneId()

        self.avatarExitEvents = []
        self.toons = []
        self.toonSkillPtsGained = {}
        self.toonExp = {}
        self.toonOrigQuests = {}
        self.toonItems = {}
        self.toonOrigMerits = {}
        self.toonMerits = {}
        self.toonParts = {}
        self.helpfulToons = []

        self.currentFloor = 0
        # There is no top floor >:)
        self.topFloor = float('inf')
        self.bldg = elevator.bldg
        self.elevator = elevator

        self.suits = []
        self.activeSuits = []
        self.reserveSuits = []
        self.joinedReserves = []
        self.suitsKilled = []
        self.suitsKilledPerFloor = []
        self.battle = None

        self.timer = Timer.Timer()

        self.responses = {}
        self.ignoreResponses = 0
        self.ignoreElevatorDone = 0
        self.ignoreReserveJoinDone = 0

        # Register all the toons
        self.toonIds = copy.copy(elevator.seats)
        for toonId in self.toonIds:
            if (toonId != None):
                self.__addToon(toonId)



        self.fsm = ClassicFSM.ClassicFSM(
            'DistributedEndlessSuitInteriorAI',
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
                         ['ReservesJoining',
                          'BattleDone']),
             State.State('ReservesJoining',
                         self.enterReservesJoining,
                         self.exitReservesJoining,
                         ['Battle']),
             State.State('BattleDone',
                         self.enterBattleDone,
                         self.exitBattleDone,
                         ['Resting',
                          'Reward']),
             State.State('Resting',
                         self.enterResting,
                         self.exitResting,
                         ['Elevator']),
             State.State('Reward',
                         self.enterReward,
                         self.exitReward,
                         ['Elevator']),
             State.State('Off',
                         self.enterOff,
                         self.exitOff,
                         ['WaitForAllToonsInside'])],
            # Initial state
            'Off',
            # Final state
            'Off',
            onUndefTransition=ClassicFSM.ClassicFSM.ALLOW)
        self.fsm.enterInitialState()

    def __addToon(self, toonId):
        if toonId not in self.air.doId2do:
            self.notify.warning('addToon() - no toon for doId: %d' % toonId)
            return

        # Handle unexpected exits for the toon
        event = self.air.getAvatarExitEvent(toonId)
        self.avatarExitEvents.append(event)
        self.accept(event, self.__handleUnexpectedExit, extraArgs=[toonId])

        self.toons.append(toonId)
        self.responses[toonId] = 0

    def __removeToon(self, toonId):
        # Reward the player based on last checkpoint
        toon = self.air.doId2do.get(toonId)
        self.rewardToon(toon)
        if self.toons.count(toonId):
            self.toons.remove(toonId)

        if self.toonIds.count(toonId):
            self.toonIds[self.toonIds.index(toonId)] = None

        if toonId in self.responses:
            del self.responses[toonId]

        # Ignore future exit events for the toon
        event = self.air.getAvatarExitEvent(toonId)
        if self.avatarExitEvents.count(event):
            self.avatarExitEvents.remove(event)
        self.ignore(event)

    def __handleUnexpectedExit(self, toonId):
        self.notify.warning('toon: %d exited unexpectedly' % toonId)
        self.__removeToon(toonId)
        if (len(self.toons) == 0):
            assert(self.notify.debug('last toon is gone!'))
            self.timer.stop()
            # The last toon exited unexpectedly - if we're in a battle, let
            # the battle clean up first, if we're in Resting state, let
            # the interior elevator clean up first, otherwise, just
            # reset the suit interior.

            # Reward the player based
            if (self.fsm.getCurrentState().getName() == 'Resting'):
                pass
            elif (self.battle == None):
                self.bldg.deleteSuitInterior()

    def elevatorDone(self):
        """elevatorDone(self)
        This message is sent from a client toon to indicate that it has
        finished viewing the elevator movie.
        """
        toonId = self.air.getAvatarIdFromSender()
        if (self.ignoreResponses == 1):
            assert(self.notify.debug('elevatorDone() ignoring toon: %d' % \
                toonId))
            return
        elif (self.fsm.getCurrentState().getName() != 'Elevator'):
            self.notify.warning('elevatorDone() - in state: %s' % \
                self.fsm.getCurrentState().getName())
            return
        elif (self.toons.count(toonId) == 0):
            self.notify.warning('elevatorDone() - toon not in toon list: %d' \
                % toonId)
            assert(self.notify.debug('toons: %s toonIds: %s' % \
                        (self.toons, self.toonIds)))
            return
        assert(toonId in self.responses)
        self.responses[toonId] += 1
        assert(self.notify.debug('toon: %d done with elevator' % toonId))
        if (self.__allToonsResponded() and
            self.ignoreElevatorDone == 0 and  self.currFloor % 5 != 0):
            self.b_setState('Battle')
        elif (self.__allToonsResponded() and
            self.ignoreElevatorDone == 0 and self.currFloor % 5 == 0):
            self.b_setState('Resting')

    def __createFloorBattle(self):
        assert (len(self.toons) > 0)
        if (self.currentFloor %4 == 0):
            assert (self.notify.debug('createFloorBattle() - boss battle'))
            bossBattle = 1
        else:
            bossBattle = 0
        # Create the battle for the floor
        self.battle = DistributedBattleBldgAI.DistributedBattleBldgAI(
            self.air, self.zoneId,
            self.__handleRoundDone, self.__handleBattleDone,
            bossBattle=bossBattle)

        # We store the lists of experience gained and suits killed in
        # the DistributedSuitInterior object, and share these pointers
        # in all battles created for this building.  This way, each
        # battle will actually be modifying the same objects, these,
        # and will thus accumulate the experience from previous
        # battles.
        self.battle.suitsKilled = self.suitsKilled
        self.battle.suitsKilledPerFloor = self.suitsKilledPerFloor
        self.battle.battleCalc.toonSkillPtsGained = self.toonSkillPtsGained
        self.battle.toonExp = self.toonExp
        self.battle.toonOrigQuests = self.toonOrigQuests
        self.battle.toonItems = self.toonItems
        self.battle.toonOrigMerits = self.toonOrigMerits
        self.battle.toonMerits = self.toonMerits
        self.battle.toonParts = self.toonParts
        self.battle.helpfulToons = self.helpfulToons

        # We must set the members of a building battle before we
        # generate it.
        self.battle.setInitialMembers(self.toons, self.suits)
        self.battle.generateWithRequired(self.zoneId)

        # We get a bonus factor applied toward each attack's experience credit.

        # Have constant double exp multiplier in building
        # Also have the highest multiplier be consistent throughought the building
        mult = getCreditMultiplier(6)

        # If there is an invasion, multiply the exp for the duration of this battle
        # Now, if the invasion ends midway through this battle, the players will
        # continue getting credit. This is ok I guess.
        #    if self.air.suitInvasionManager.getInvading():
        # mult *= getInvasionMultiplier()

        self.battle.battleCalc.setSkillCreditMultiplier(mult)

    def __cleanupFloorBattle(self):
        for suit in self.suits:
            self.notify.debug('cleaning up floor suit: %d' % suit.doId)
            if suit.isDeleted():
                self.notify.debug('whoops, suit %d is deleted.' % suit.doId)
            else:
                suit.requestDelete()
        self.suits = []
        self.reserveSuits = []
        self.activeSuits = []
        if (self.battle != None):
            self.battle.requestDelete()
        self.battle = None

    def __handleRoundDone(self, toonIds, totalHp, deadSuits):
        # Determine if any reserves need to join
        assert(self.notify.debug('handleRoundDone() - hp: %d' % totalHp))
        # Calculate the total max HP for all the suits currently on the floor
        totalMaxHp = 0
        for suit in self.suits:
            totalMaxHp += suit.maxHP

        for suit in deadSuits:
            self.activeSuits.remove(suit)

        # Determine if any reserve suits need to join
        if (len(self.reserveSuits) > 0 and len(self.activeSuits) < 4):
            self.joinedReserves = []
            hpPercent = 100 - (totalHp / totalMaxHp * 100.0)
            for info in self.reserveSuits:
                if (info[1] <= hpPercent and
                    len(self.activeSuits) < 4):
                    self.suits.append(info[0])
                    self.activeSuits.append(info[0])
                    self.joinedReserves.append(info)
            for info in self.joinedReserves:
                self.reserveSuits.remove(info)
            if (len(self.joinedReserves) > 0):
                # setSuits() triggers the state change on the client
                self.fsm.request('ReservesJoining')
                self.d_setSuits()
                return

        # See if the battle is done
        if (len(self.activeSuits) == 0):
            self.fsm.request('BattleDone', [toonIds])
        else:
            # No reserve suits to join - tell the battle to continue
            self.battle.resume()

    def __handleBattleDone(self, zoneId, toonIds):
        # self.fsm.request('BattleDone', [toonIds])
        if (len(toonIds) == 0):
            # Rather than shutting down immediately, we give the last
            # toon a few seconds to finish playing his teleport-out
            # animation before the world goes away.

            taskName = self.taskName('deleteInterior')
            taskMgr.doMethodLater(10, self.__doDeleteInterior, taskName)

            # This is not b_setState, because enterReward has to do
            # some things before the broadcast takes place. enterReward
            # will call d_setState when it is ready.

        # We give reward every floor
        # TODO since this calls battlebase we need to check in battlebase if we are in an endless building skip the reward visual
        self.setState('Reward')
        self.b_setState('Resting')

    def enterBattle(self):
        if (self.battle == None):
            self.__createFloorBattle()
            self.elevator.d_setFloor(self.currentFloor)
        return None

    def exitBattle(self):
        return None


##### BattleDone state #####

    def enterBattleDone(self, toonIds):
        # Find out if any toons are gone
        if (len(toonIds) != len(self.toons)):
            deadToons = []
            for toon in self.toons:
                if (toonIds.count(toon) == 0):
                    deadToons.append(toon)
            for toon in deadToons:
                self.__removeToon(toon)
        self.d_setToons()

        if (len(self.toons) == 0):
            self.bldg.deleteSuitInterior()
        else:
           # if (self.currentFloor == self.topFloor):
           #     # Toons beat the building
            #    self.battle.resume(self.currentFloor, topFloor=1)
            #else:
                # The building isn't finished yet - gather up experience and
                # activate the elevator
            self.battle.resume(self.currentFloor, topFloor=0)
        return None


    def exitBattleDone(self):
        self.__cleanupFloorBattle()
        return None

    def rewardToon(self, toon):
        # whatever extra rewards we want go here
        return


##### Reward state #####

    def enterReward(self):

        #Tell the client its reward time
        self.d_setState('Reward')
        return None