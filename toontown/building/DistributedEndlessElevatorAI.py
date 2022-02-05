from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.task import Task
from otp.ai.AIBase import *
from toontown.building import DistributedElevatorExtAI
from toontown.building.ElevatorConstants import *
from toontown.toonbase import ToontownGlobals
from . import SuitPlannerEndlessInteriorAI

from . import DistributedEndlessSuitInteriorAI

class DistributedEndlessElevatorAI(DistributedElevatorExtAI.DistributedElevatorExtAI):

    def __init__(self, air, bldg, antiShuffle=0, minLaff=0, endlessId = None, entranceId= None):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(
            self, air, bldg, antiShuffle=antiShuffle, minLaff=minLaff)

        # add in the future
        # self.endlessId = endlessId
        # self.entranceId = entranceId
        self.planner = None

    def getEntranceId(self):
        return
        # return self.entranceId

    def _createSuitInterior(self, interiorZoneId):
        return DistributedEndlessSuitInteriorAI.DistributedEndlessSuitInteriorAI(self.air,
                                                                   self, interiorZoneId)

    def createSuitInterior(self):
        # Create a building interior in the new (interior) zone
        dummy, interiorZoneId = self.air.allocateZone()
        self.planner = SuitPlannerEndlessInteriorAI.SuitPlannerEndlessInteriorAI(
            interiorZoneId)
        self.interior = self._createSuitInterior()
        
        self.interior.fsm.request('WaitForAllToonsInside')
        self.interior.generateWithRequired(interiorZoneId)

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()

        # It is possible the players exited the district
        if (numPlayers > 0):
            self._createInterior()
            for seatIndex in range(len(self.seats)):
                avId = self.seats[seatIndex]
                # Tell each player on the elevator that they should enter the
                # building now.
                if avId:
                    assert(avId > 0)
                    # Clear the fill slot
                    self.clearFullNow(seatIndex)
        else:
            self.notify.warning("The elevator left, but was empty.")
        self.fsm.request("closed")

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        # Switch back into opening mode since we allow other Toons onboard
        self.fsm.request('opening')


