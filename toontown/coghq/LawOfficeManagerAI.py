from direct.directnotify import DirectNotifyGlobal
from . import DistributedLawOfficeAI
from . import DistributedStageAI
from toontown.coghq import StageLayout
from toontown.toonbase import ToontownGlobals
from direct.showbase import DirectObject
import random


StageId2Layouts = {
    ToontownGlobals.LawbotStageIntA: (0, 1, 2, ),
    ToontownGlobals.LawbotStageIntB: (3, 4, 5, ),
    ToontownGlobals.LawbotStageIntC: (6, 7, 8, ),
    ToontownGlobals.LawbotStageIntD: (9, 10, 11,),
}


class LawOfficeManagerAI(DirectObject.DirectObject):

    notify = DirectNotifyGlobal.directNotify.newCategory('LawOfficeManagerAI')

    # magic-word override
    lawOfficeId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        # DistributedElevatorAI needs this
        return 0

    def createLawOffice(self, StageId, entranceId, players):
        # check for ~StageId
        for avId in players:
            if bboard.has(f'StageId-{avId}'):
                StageId = bboard.get(f'StageId-{avId}')
                break

        floor = 0
        layoutIndex = None

        # check for ~StageRoom
        for avId in players:
            if bboard.has(f'stageRoom-{avId}'):
                roomId = bboard.get(f'stageRoom-{avId}')
                for lt in StageId2Layouts[StageId]:
                    for i in range(StageLayout.getNumFloors(lt)):
                        layout = StageLayout.StageLayout(
                            StageId, i, stageLayout=lt)
                        if roomId in layout.getRoomIds():
                            layoutIndex = lt
                            floor = i
                else:
                    from toontown.coghq import StageRoomSpecs
                    roomName = StageRoomSpecs.CashbotStageRoomId2RoomName[roomId]
                    LawOfficeManagerAI.notify.warning(
                        'room %s (%s) not found in any floor of Stage %s' %
                        (roomId, roomName, StageId))

        StageZone = self.air.allocateZone()
        if layoutIndex is None:
            layoutIndex = random.choice(StageId2Layouts[StageId])
        Stage = DistributedStageAI.DistributedStageAI(
            self.air, StageId, StageZone, floor, players, layoutIndex)
        Stage.generateWithRequired(StageZone)
        return StageZone
