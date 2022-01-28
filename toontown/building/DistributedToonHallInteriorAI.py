from .DistributedToonInteriorAI import *
from toontown.toonbase import ToontownGlobals


class DistributedToonHallInteriorAI(DistributedToonInteriorAI):
    """
    DistributedToonHallInteriorAI class:
    """

    if __debug__:
        notify = DirectNotifyGlobal.directNotify.newCategory(
            'DistributedToonHallInteriorAI')

    def __init__(self, block, air, zoneId, building):
        DistributedToonInteriorAI.__init__(self, block, air, zoneId, building)

        self.accept("ToonEnteredZone", self.logToonEntered)
        self.accept("ToonLeftZone", self.logToonLeft)

    def logToonEntered(self, avId, zoneId):
        result = self.getCurPhase()
        if result == -1:
            phase = "not available"
        else:
            phase = str(result)
        self.air.writeServerEvent('sillyMeter', avId, f'enter|{phase}')

    def logToonLeft(self, avId, zoneId):
        result = self.getCurPhase()
        if result == -1:
            phase = "not available"
        else:
            phase = str(result)
        self.air.writeServerEvent('sillyMeter', avId, f'exit|{phase}')

    def getCurPhase(self):
        result = -1
        enoughInfoToRun = False
        # first see if the holiday is running, and we can get the cur phase
        if ToontownGlobals.SILLYMETER_HOLIDAY in simbase.air.holidayManager.currentHolidays \
            and simbase.air.holidayManager.currentHolidays[ToontownGlobals.SILLYMETER_HOLIDAY] is not None \
                and simbase.air.holidayManager.currentHolidays[ToontownGlobals.SILLYMETER_HOLIDAY].getRunningState():
            if hasattr(simbase.air, "SillyMeterMgr"):
                enoughInfoToRun = True
            else:
                self.notify.debug("simbase.air does not have SillyMeterMgr")
        else:
            self.notify.debug("holiday is not running")
        self.notify.debug(f"enoughInfoToRun = {enoughInfoToRun}")
        if enoughInfoToRun and \
           simbase.air.SillyMeterMgr.getIsRunning():
            result = simbase.air.SillyMeterMgr.getCurPhase()
        return result

    def delete(self):
        assert(self.debugPrint("delete()"))
        self.ignoreAll()
        DistributedToonInteriorAI.delete(self)
