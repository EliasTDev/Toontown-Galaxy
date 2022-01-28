from direct.distributed import DistributedObjectAI
from otp.level import DistributedLevelAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.coghq import CountryClubLayout, DistributedCountryClubRoomAI
from toontown.coghq import BattleExperienceAggregatorAI
from toontown.building import DistributedClubElevatorAI


class DistributedCountryClubAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedCountryClubAI')

    def __init__(
            self,
            air,
            countryClubId,
            zoneId,
            floorNum,
            avIds,
            layoutIndex,
            battleExpAggreg=None):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.countryClubId = countryClubId
        self.zoneId = zoneId
        self.floorNum = floorNum
        self.avIds = avIds
        self.layoutIndex = layoutIndex
        self.blockedRooms = []
        self.elevatorList = []
        self.battleExpAggreg = battleExpAggreg
        self.layout = CountryClubLayout.CountryClubLayout(
            self.countryClubId, self.floorNum, self.layoutIndex)
        for i in range(self.layout.getNumRooms()):
            if i:
                self.blockedRooms.append(i)

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.notify.info('generate %s, id=%s, floor=%s' %
                         (self.doId, self.countryClubId, self.floorNum))

        self.rooms = []

        # create a battle experience aggregator for the countryClub rooms to
        # share
        if self.battleExpAggreg is None:
            self.battleExpAggreg = BattleExperienceAggregatorAI.\
                BattleExperienceAggregatorAI()

        # create a CountryClubRoom level obj for each room in the layout
        for i in range(self.layout.getNumRooms()):
            # i*2 for roomNum leaves numbers for hallways
            room = DistributedCountryClubRoomAI.DistributedCountryClubRoomAI(
                self.air, self.countryClubId, self.doId, self.zoneId,
                self.layout.getRoomId(i), i * 2, self.avIds,
                self.battleExpAggreg)
            room.generateWithRequired(self.zoneId)
            self.rooms.append(room)

        roomDoIds = []
        for room in self.rooms:
            roomDoIds.append(room.doId)
        self.sendUpdate('setRoomDoIds', [roomDoIds])

        self.placeElevatorsOnMarkers()

        if __dev__:
            simbase.countryClub = self

        # log that toons entered the countryClub
        description = f'{self.countryClubId}|{self.floorNum}|{self.avIds}'
        for avId in self.avIds:
            self.air.writeServerEvent('countryClubEntered', avId, description)

    def requestDelete(self):
        self.notify.info(f'requestDelete: {self.doId}')
        for room in self.rooms:
            room.requestDelete()
        if hasattr(self, "elevatorList"):
            for elevator in self.elevatorList:
                elevator.requestDelete()
        DistributedObjectAI.DistributedObjectAI.requestDelete(self)

    def delete(self):
        self.notify.info(f'delete: {self.doId}')
        if __dev__:
            if hasattr(simbase, 'countryClub') and simbase.countryClub is self:
                del simbase.countryClub
        del self.rooms
        del self.layout
        del self.battleExpAggreg
        if hasattr(self, "elevatorList"):
            del self.elevatorList
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getTaskZoneId(self):
        return self.countryClubId

    def allToonsGone(self):
        # the countryClub room objs clean themselves up; in fact, the first countryClub
        # room will call this for us when it detects that all toons have
        # left
        self.notify.info('allToonsGone')
        self.requestDelete()

    # required-field getters
    def getZoneId(self):
        return self.zoneId

    def getCountryClubId(self):
        return self.countryClubId

    def getFloorNum(self):
        return self.floorNum

    def getBlockedRooms(self):
        self.notify.debug(f'getBlockedRooms returning {self.blockedRooms}')
        return self.blockedRooms

    def roomDefeated(self, room):
        """Handle the room telling us its challenge has been defeated."""
        # remove the room in self.blockedRooms and tell the clients
        if room in self.rooms:
            roomIndex = self.rooms.index(room)
            if roomIndex in self.blockedRooms:
                self.blockedRooms.remove(roomIndex)
                self.sendUpdate('setBlockedRooms', [self.blockedRooms])

    def placeElevatorsOnMarkers(self):
        for room in self.rooms:
            if room.entType2ids['elevatorMarker']:
                for markerId in room.entType2ids['elevatorMarker']:
                    marker = room.getEntity(markerId)
                    newElevator = DistributedClubElevatorAI.DistributedClubElevatorAI(
                        self.air, self.doId, self, self.avIds, marker.doId)
                    # newElevator.setLatch(marker.doId)
                    newElevator.generateWithRequired(self.zoneId)
                    self.elevatorList.append(newElevator)

    def startNextFloor(self):
        floor = self.floorNum + 1

        countryClubZone = self.air.allocateZone()
        # (self, air, countryClubId, zoneId, floorNum, avIds):
        countryClub = DistributedCountryClubAI(
            self.air, self.countryClubId, countryClubZone, floor, self.avIds,
            self.layoutIndex, self.battleExpAggreg)
        countryClub.generateWithRequired(countryClubZone)

        for avId in self.avIds:
            #print("SENDING SETCOUNTRYCLUBZONE %s" % (avId))
            self.sendUpdateToAvatarId(
                avId, "setCountryClubZone", [countryClubZone])
        self.requestDelete()

    def elevatorAlert(self, avId):
        self.sendUpdate("elevatorAlert", [avId])

    def setLayoutIndex(self, layoutIndex):
        self.layoutIndex = layoutIndex

    def getLayoutIndex(self):
        return self.layoutIndex
