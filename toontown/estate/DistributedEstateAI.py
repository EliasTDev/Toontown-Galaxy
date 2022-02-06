
from otp.ai.AIBase import *
from direct.distributed.ClockDelta import *
from toontown.toonbase.ToontownGlobals import *
from otp.otpbase import OTPGlobals
from otp.ai.AIZoneData import AIZoneData
from direct.distributed import DistributedObjectAI
from . import DistributedHouseAI
#import DistributedPlantAI
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
import random
import pickle
from . import HouseGlobals
#from toontown.safezone import DistributedButterflyAI
from toontown.safezone import ButterflyGlobals
from toontown.safezone import ETreasurePlannerAI
from toontown.safezone import DistributedPicnicTableAI
from toontown.safezone import DistributedChineseCheckersAI
from . import DistributedTargetAI
from toontown.estate import DistributedFlowerAI
from toontown.estate import DistributedGagTreeAI
from toontown.estate import DistributedStatuaryAI
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.estate import DistributedChangingStatuaryAI
from toontown.estate import DistributedToonStatuaryAI
from toontown.fishing.DistributedFishingPondAI import DistributedFishingPondAI
from toontown.safezone.DistributedFishingSpotAI import DistributedFishingSpotAI
from toontown.safezone import EFlyingTreasurePlannerAI
from . import DistributedCannonAI
from panda3d.toontown import *

class DistributedEstateAI(DistributedObjectAI.DistributedObjectAI):

    """
    This is the class that handles the creation of an estate and all
    things contained in an estate, including:  houses, ponds, gardens,
    mailboxes, etc.
    """

    notify = directNotify.newCategory("DistributedEstateAI")
    #notify.setDebug(True)

    printedLs = 0

    EstateModel = None

    dayInSeconds = 24 * 60 * 60

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

        # the avatar currently in charge of the estate
        #self.notify.info("created with avId = %d and zoneId = %d" % (avId, zoneId))
        #self.avId = 0
        #self.zoneId = 0

        #simbase.air.lastEstate = self inable to check the estate.
        self.houses = [None] * 6
        self.estateType = 0
        if not hasattr(self, 'avId'):
            self.avId = 0
        if not hasattr(self, 'zoneId'):
            self.zoneId = 0
        self.estateButterflies = None
        self.fishingSpots = None
        self.fishingPonds = None
        self.goons = None
        self.estateTreasurePlanner = None
        self.estateFlyingTreasurePlanner = None
        self.estateFireworks = None
        self.target = None
        self.picnicTable = None

        self.houseList = []
        self.idList = []
        #if not hasattr(self, "decorData"):
        #    self.decorData = []

        self.cannonsEnabled = simbase.config.GetBool('estate-cannons', 0)
        self.fireworksEnabled = simbase.config.GetBool('estate-fireworks', 0)
        self.goonEnabled = simbase.config.GetBool('estate-goon', 0) #what is this 
        self.goons = None
        self.gagBarrels = None
        self.crate = None

        self.cannonFlag = 0
        self.gameTableFlag = False

        # for day/night
        #self.serverTime = ts
        self.dawnTime = 0

        #here we load in all the database fields
        #if valDict:
          #  for key in valDict:
           #     if hasattr(self, key):
           #         self.dclass.directUpdate(self, key, valDict[key])

        # keep track of generation/deletion from stateserver
        #self.Estate_generated = 0

        #testFlower = DistributedFlowerAI.DistributedFlowerAI()
        #testGagTree = DistributedGagTreeAI.DistributedGagTreeAI()
        #testStatuary = DistributedStatuaryAI.DistributedStatuaryAI()

        if not hasattr(self, "lastEpochTimeStamp"):
            self.lastEpochTimeStamp = time.time()



        self.maxSlots = 32
        self.toonsPerAccount = 6
        #self.timePerEpoch = 300 #five minutes
        #self.timePerEpoch = 30000 #5000 minutes #NO LONGER A VALID CONCEPT AS EPOCHS HAPPEN ONCE A DAY


    def announceGenerate(self):
        DistributedObjectAI.DistributedObjectAI.announceGenerate(self)
        self.initEstateData()
        self.createPetCollisions()

    def generate(self):
        DistributedEstateAI.notify.info("DistEstate generate: %s" % self.doId)
        #self.Estate_generated = 1
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def generateWithRequiredAndId(self, doId, air, zoneId):
        self.notify.info("DistributedEstateAI generateWithRequiredAndId")

        DistributedObjectAI.DistributedObjectAI.generateWithRequiredAndId(self, doId, air, zoneId)

#    def requestDelete(self):
#        taskMgr.remove(self.uniqueName("GardenEpoch"))
#        taskMgr.remove(self.uniqueName("endCannons"))
#        taskMgr.remove(self.uniqueName("endCannonsNotify"))
#        DistributedObjectAI.DistributedObjectAI.requestDelete(self)

    def delete(self):
        DistributedEstateAI.notify.info("DistEstate delete: %s" % self.doId)
        self.ignoreAll()
        taskMgr.remove(self.uniqueName("endCannons"))
        taskMgr.remove(self.uniqueName("endCannonsNotify"))
        taskMgr.remove(self.uniqueName("endGameTable"))
        #print("Trying Delete Estate")
        try:
            #print("checking already deleted")
            self.Estate_deleted
            DistributedEstateAI.notify.info("estate already deleted: %s" % self.Estate_deleted)
        except:
            #print("deleting Estate")
            DistributedEstateAI.notify.info("completing estate delete: %s" % self.__dict__.get("zoneId"))
            self.Estate_deleted = self.zoneId

            if self.estateTreasurePlanner:
                self.estateTreasurePlanner.stop()
                self.estateTreasurePlanner.deleteAllTreasuresNow()
                self.estateTreasurePlanner = None

            if self.estateFlyingTreasurePlanner:
                self.estateFlyingTreasurePlanner.stop()
                self.estateFlyingTreasurePlanner.deleteAllTreasuresNow()
                self.estateFlyingTreasurePlanner = None

            if self.estateButterflies:
                for bfly in self.estateButterflies:
                    bfly.fsm.requestFinalState()
                    bfly.requestDelete()
                self.estateButterflies = None
                ButterflyGlobals.clearIndexes(self.avId)

            if self.fishingSpots:
                for spot in self.fishingSpots:
                    spot.requestDelete()
                self.fishingSpots = None

            if self.fishingPonds:
                for pond in self.fishingPonds:
                    # Remove PondBingoManager
                    if simbase.wantBingo:
                        if pond.hasPondBingoManager():
                            pond.getPondBingoManager().requestDelete()
                    pond.requestDelete()
                self.fishingPonds = None

            if self.estateFireworks:
                self.estateFireworks.requestDelete()
                del self.estateFireworks

            if hasattr(self, "target"):
                if self.target:
                    self.target.requestDelete()
                    del self.target

            if self.goons:
                for goon in self.goons:
                    goon.requestDelete()
                    del goon
                self.goons = None

            if self.gagBarrels:
                for barrel in self.gagBarrels:
                    barrel.requestDelete()
                    del barrel
                self.gagBarrels = None

            if self.crate:
                del self.crate
                self.crate = None

            if self.picnicTable:
                self.picnicTable.requestDelete()
                del self.picnicTable
                self.picnicTable = None

            del self.houseList



            DistributedObjectAI.DistributedObjectAI.delete(self)

    def unload(self):
        self.notify.info("unload")

  


    def destroy(self):
        for house in self.houses:
            if house is not None:
                house.requestDelete()

        del self.houses[:]
        self.requestDelete()
        
    def initEstateData(self, estateVal=None, numHouses=0, houseId=None, houseVal=None):
        # these parameters have just been read from the database..
        # now we have to do something with them.
        self.numHouses = numHouses
        self.houseType = [None] * self.numHouses
        self.housePos = [None] * self.numHouses
        self.houseId = houseId
        self.houseVal = houseVal
        self.estateVal = estateVal

        # start treasure planner
        self.estateTreasurePlanner = ETreasurePlannerAI.ETreasurePlannerAI(self.zoneId)
        self.estateTreasurePlanner.start()

        # start butterflies
        self.estateButterflies = []
       # if simbase.config.GetBool('want-estate-butterflies', 0):
       #     ButterflyGlobals.generateIndexes(self.avId, ButterflyGlobals.ESTATE)
       #     for i in range(0,
       #             ButterflyGlobals.NUM_BUTTERFLY_AREAS[ButterflyGlobals.ESTATE]):
               # for j in range(0,
        #            ButterflyGlobals.NUM_BUTTERFLIES[ButterflyGlobals.ESTATE]):
                    #bfly = DistributedButterflyAI.DistributedButterflyAI(self.air,
                    #                     ButterflyGlobals.ESTATE, i, self.avId)
                    #bfly.generateWithRequired(self.zoneId)
                    #bfly.start()
                    #self.estateButterflies.append(bfly)

        # Create fishing docks
        dnaStore = DNAStorage()
        dnaData = simbase.air.loadDNAFileAI(dnaStore,
                  simbase.air.lookupDNAFileName('estate_1.dna'))
        self.fishingSpots = []
        self.fishingPonds = []
        if (isinstance(dnaData, DNAData)):
            fishingPonds, fishingPondGroups = self.air.findFishingPonds(dnaData, self.zoneId, MyEstate, overrideDNAZone = 1)
            self.fishingPonds += fishingPonds
            for dnaGroup, distPond in zip(fishingPondGroups, fishingPonds):
                self.fishingSpots += self.air.findFishingSpots(dnaGroup, distPond)
        else:
            self.notify.warning("loadDNAFileAI failed for 'estate_1.dna'")

        if simbase.wantPets:

            if not DistributedEstateAI.EstateModel:
                # load up the estate model for the pets
                self.dnaStore = DNAStorage()
                simbase.air.loadDNAFile(
                    self.dnaStore,
                    self.air.lookupDNAFileName('storage_estate.dna'))
                node = simbase.air.loadDNAFile(
                    self.dnaStore,
                    self.air.lookupDNAFileName('estate_1.dna'))
                DistributedEstateAI.EstateModel = hidden.attachNewNode(
                    node)
            render = self.getRender()
            self.geom = DistributedEstateAI.EstateModel.copyTo(render)
            # for debugging, show what's in the model
            if not DistributedEstateAI.printedLs:
                DistributedEstateAI.printedLs = 1
                #self.geom.ls()

            if 0:#__dev__:
                pt.mark('loaded estate model')
                pt.off()
                pt.printTo()

        if self.fireworksEnabled:
            pos = (29.7, -1.77, 10.93)
            from . import DistributedFireworksCannonAI
            self.estateFireworks = DistributedFireworksCannonAI.DistributedFireworksCannonAI(self.air, *pos)
            self.estateFireworks.generateWithRequired(self.zoneId)

        if self.goonEnabled:
            from toontown.suit import DistributedGoonAI
            self.goons = [None]*3
            for i in range(3):
                self.goons[i] = DistributedGoonAI.DistributedGoonAI(self.air,None,i)
                self.goons[i].setupSuitDNA(1, 1, "c")
                self.goons[i].generateWithRequired(self.zoneId)

            from toontown.coghq import DistributedGagBarrelAI
            self.gagBarrels = [None]*4
            for i in range(4):
                self.gagBarrels[i] = DistributedGagBarrelAI.DistributedGagBarrelAI(self.air, None,
                                                                                   -100-10*i, 30-10*i, 0.2,i,i)
                self.gagBarrels[i].generateWithRequired(self.zoneId)
            from toontown.coghq import DistributedBeanBarrelAI
            jelly = DistributedBeanBarrelAI.DistributedBeanBarrelAI(self.air, None,-150, -20, 0.2)
            jelly.generateWithRequired(self.zoneId)
            self.gagBarrels.append(jelly)

            from toontown.coghq import DistributedCrateAI
            self.crate = DistributedCrateAI.DistributedCrateAI(self.air, -142, 0, 0.0)
            self.crate.generateWithRequired(self.zoneId)

        #self.testPlant = DistributedPlantAI.DistributedPlantAI(self.air)
        #self.testPlant.generateWithRequired(self.zoneId)
        #self.placeOnGround(self.testPlant.doId)
        simbase.estate = self
        #self.b_setDecorData([[2,[0,42,42,1],[512,1024,2048]],[1,[2,3],[512,1024,2048]]])
        #self.air.queryObjectField("DistributedEstate", "setDecorData", self.doId, None)
        #self.b_setDecorData([[1,0,16,16,0]])

    def postHouseInit(self):
        #print("post house Init")

        currentTime = time.time()
        #print("time: %s \n cts:%s" % (currentTime, self.rentalTimeStamp))
        if self.rentalTimeStamp >= currentTime:
            #print("starting cannons")
            if self.rentalType == ToontownGlobals.RentalCannon:
                self.makeCannonsUntil(self.rentalTimeStamp)
            elif self.rentalType == ToontownGlobals.RentalGameTable:
                self.makeGameTableUntil(self.rentalTimeStamp)
        else:
            self.b_setRentalTimeStamp(0)
            pass
            #print("not starting cannons")

    def startCannons(self, fool = 0):
        if self.cannonFlag:
            return
        # create flying treasures
        if not self.estateFlyingTreasurePlanner:
            self.estateFlyingTreasurePlanner = EFlyingTreasurePlannerAI.EFlyingTreasurePlannerAI(self, self.zoneId)
        self.estateFlyingTreasurePlanner.preSpawnTreasures()
        self.estateFlyingTreasurePlanner.start()

        # tell client about flying treasures
        self.updateFlyingTreasureList()

        # create the target
        if not hasattr(self, "target") or not self.target:
            self.target = DistributedTargetAI.DistributedTargetAI(self.air, -5.6, -24, 50)
            self.target.generateWithRequired(self.zoneId)
        self.target.start()

        for house in self.houseList:
            house.setCannonEnabled(1)

        self.b_setClouds(1)
        self.cannonFlag = 1

    def endCannons(self, fool = 0):
        if not self.cannonFlag:
            return
        for house in self.houseList:
            house.setCannonEnabled(0)
        self.b_setClouds(0)

        if self.estateFlyingTreasurePlanner:
            self.estateFlyingTreasurePlanner.stop()
            self.estateFlyingTreasurePlanner.deleteAllTreasuresNow()

        if hasattr(self, "target"):
            if self.target:
                self.target.requestDelete()
                del self.target

        self.b_setRentalTimeStamp(0)
        self.cannonFlag = 0

    def notifyCannonsEnd(self, arg=None):
        self.sendUpdate("cannonsOver", [])

    def bootStrapEpochs(self):
        #first update the graden data based on how much time has based
        print ("last time %s" % (self.lastEpochTimeStamp))
        currentTime = time.time()
        print ("current time %s" % (currentTime))
        timeDiff = currentTime - self.lastEpochTimeStamp
        print ("time diff %s" % (timeDiff))
        
        #self.lastEpochTimeStamp = time.mktime((2006, 8, 24, 10, 50, 31, 4, 237, 1))
        if self.lastEpochTimeStamp == 0:
            self.lastEpochTimeStamp = time.time()
        tupleNewTime = time.localtime(currentTime - self.epochHourInSeconds)
        tupleOldTime = time.localtime(self.lastEpochTimeStamp)

        #tupleOldTime = (2006, 6, 18, 0, 36, 45, 0, 170, 1)
        #tupleNewTime = (2006, 6, 19, 3, 36, 45, 0, 170, 1)

        listLastDay = list(tupleOldTime)
        listLastDay[3] = 0 #set hour to epoch time
        listLastDay[4] = 0 #set minute to epoch time
        listLastDay[5] = 0 #set second to epoch time
        tupleLastDay = tuple(listLastDay)

        randomDelay = random.random() * 5 * 60 # random five minute range
        #this isnt even used wth disney
        #secondsNextEpoch = ((time.mktimetupleLastDay) + self.epochHourInSeconds + self.dayInSeconds + randomDelay) - currentTime
        
        #should we do the epoch for the current day?
        #beforeEpoch = 1
        #if  tupleNewTime[3] >= self.timeToEpoch:
        #    beforeEpoch = 0

        epochsToDo =  int((time.time() - time.mktime(tupleLastDay)) / self.dayInSeconds)
        #epochsToDo -= beforeEpoch
        if epochsToDo < 0:
            epochsToDo = 0

        print(("epochsToDo %s" % (epochsToDo)))

        #print("tuple times")
        #print tupleNewTime
        #print tupleOldTime


        if epochsToDo:
            pass
            print("doingEpochData")
            self.doEpochData(0, epochsToDo)
        else:
            pass
            print("schedualing next Epoch")
            #print("Delaying inital epoch")
            self.scheduleNextEpoch()
            self.sendUpdate("setLastEpochTimeStamp", [self.lastEpochTimeStamp])
            #time2Epoch = self.timePerEpoch - timeDiff


    def scheduleNextEpoch(self):
        currentTime = time.time()
        tupleNewTime = time.localtime()
        tupleOldTime = time.localtime(self.lastEpochTimeStamp)

        listLastDay = list(tupleOldTime)
        listLastDay[3] = 0 #set hour to epoch time
        listLastDay[4] = 0 #set minute to epoch time
        listLastDay[5] = 0 #set second to epoch time
        tupleLastDay = tuple(listLastDay)

        randomDelay = random.random() * 5 * 60 # random five minute range
        whenNextEpoch = (time.mktime(tupleLastDay) + self.epochHourInSeconds + self.dayInSeconds + randomDelay)
        secondsNextEpoch = whenNextEpoch - currentTime
        if secondsNextEpoch >= 0:
            secondsNextEpoch += self.dayInSeconds

        tupleNextEpoch = time.localtime(whenNextEpoch)

        self.notify.info("Next epoch to happen at %s %s %s %s %s %s %s %s %s" % (tupleNextEpoch))


    def setIdList(self, idList):
        self.idList = idList

    def d_setIdList(self, idList):
        self.sendUpdate('setIdList', [idList])

    def b_setIdList(self, idList):
        self.setIdList(idList)
        self.d_setIdList(idList)


   






    def findItemAtHardPoint(self, itemList, hardPoint):
        for item in itemList:
            if hardPoint == item[1]:
                return item
        return None

    def findItemPositionInItemList(self, itemList, hardPointIndex):
        for itemListIndex in range(len(itemList)):
            if hardPointIndex == itemList[itemListIndex][1]:
                return itemListIndex
        return -1

    def placeOnGround(self, doId):
        self.sendUpdate('placeOnGround', [doId])

    def setPetIds(self, petIds):
        self.petIds = petIds

    if simbase.wantPets:
        def createPetCollisions(self):
            # call this after the world geom is all set up
            render=self.getRender()
            # find the collisions and make copies of them, centered at Z=0
            self.petColls = render.attachNewNode('petColls')
            colls = self.geom.findAllMatches('**/+CollisionNode')
            for coll in colls:
                bitmask = coll.node().getIntoCollideMask()
                if not (bitmask & BitMask32(OTPGlobals.WallBitmask)).isZero():
                    newColl = coll.copyTo(self.petColls)
                    # make sure it's still in the correct position relative
                    # to the world
                    newColl.setTransform(coll.getTransform(self.geom))
                    """
                    bounds = coll.getBounds()
                    height = abs(bounds.getMax()[2] - bounds.getMin()[2])
                    """
                    # move down two feet to account for collisions that are
                    # not at Z=0
                    newColl.setZ(render, -2)
            self.geom.stash()
            # set up the collision traverser for this zone
            self.getZoneData().startCollTrav()

    def destroyEstateData(self):
        if hasattr(self, "Estate_deleted"):
            DistributedEstateAI.notify.info("destroyEstateData: estate already deleted: %s" % self.Estate_deleted)
            return

        DistributedEstateAI.notify.info("destroyEstateData: %s" % self.__dict__.get("zoneId"))

        #if hasattr(self, 'zoneId'):
        #    DistributedEstateAI.notify.info('destroyEstateData: %s' % self.zoneId)
        #else:
        #    DistributedEstateAI.notify.info('destroyEstateData: zoneID reference deleted')

        if hasattr(self, 'geom'):
            self.petColls.removeNode()
            del self.petColls
            self.geom.removeNode()
            del self.geom
            self.releaseZoneData()
        else:
            DistributedEstateAI.notify.info('estateAI has no geom...')

    def updateFlyingTreasureList(self):
        treasures = self.estateFlyingTreasurePlanner.treasures

        doIdList = []
        for t in treasures:
            if t != None:
                doIdList.append(t.doId)
        self.sendUpdate("setTreasureIds", [doIdList])

    def getEstateType(self):
        assert(self.notify.info("getEstateType"))
        return self.estateType

    def getDawnTime(self):
        return self.dawnTime

    def requestServerTime(self):
        #print ("requestServerTime")
        requesterId = self.air.getAvatarIdFromSender()
        self.serverTime = time.time() % HouseGlobals.DAY_NIGHT_PERIOD
        self.sendUpdateToAvatarId(requesterId, "setServerTime", [self.serverTime])

    def b_setDecorData(self, decorData):
        self.setDecorData(decorData)
        self.d_setDecorData(decorData)

    def setDecorData(self, decorData):
        self.decorData = decorData
        #print ("setDecorData %s" % (self.doId))

    def d_setDecorData(self, decorData):
        print("FIXME when correct toon.dc is checked in")
        #self.sendUpdate("setDecorData", [decorData])

    def getDecorData(self):
        if hasattr(self, "decorData"):
            return self.decorData
        else:
            return []

# lots of get and set functions, not really the prettiest way to do this but it works

    def getToonId(self, slot):
        if slot == 0:
            if hasattr(self, "slot0ToonId"):
                return self.slot0ToonId
        elif slot == 1:
            if hasattr(self, "slot1ToonId"):
                return self.slot1ToonId
        elif slot == 2:
            if hasattr(self, "slot2ToonId"):
                return self.slot2ToonId
        elif slot == 3:
            if hasattr(self, "slot3ToonId"):
                return self.slot3ToonId
        elif slot == 4:
            if hasattr(self, "slot4ToonId"):
                return self.slot4ToonId
        elif slot == 5:
            if hasattr(self, "slot5ToonId"):
                return self.slot5ToonId
        else:
            return None

    def setToonId(self, slot, tag):
        if slot == 0:
            self.slot0ToonId = tag
        elif slot == 1:
            self.slot1ToonId = tag
        elif slot == 2:
            self.slot2ToonId = tag
        elif slot == 3:
            self.slot3ToonId = tag
        elif slot == 4:
            self.slot4ToonId = tag
        elif slot == 5:
            self.slot5ToonId = tag

    def d_setToonId(self, slot, avId):
        if avId:
            if slot == 0:
                self.sendUpdate("setSlot0ToonId", [avId])
            elif slot == 1:
                self.sendUpdate("setSlot1ToonId", [avId])
            elif slot == 2:
                self.sendUpdate("setSlot2ToonId", [avId])
            elif slot == 3:
                self.sendUpdate("setSlot3ToonId", [avId])
            elif slot == 4:
                self.sendUpdate("setSlot4ToonId", [avId])
            elif slot == 5:
                self.sendUpdate("setSlot5ToonId", [avId])

    def b_setToonId(self, slot, avId):
        self.setToonId(slot, avId)
        self.d_setToonId(slot, avId)

    def getItems(self, slot):
        if slot == 0:
            if hasattr(self, "slot0Items"):
                return self.slot0Items
        elif slot == 1:
            if hasattr(self, "slot1Items"):
                return self.slot1Items
        elif slot == 2:
            if hasattr(self, "slot2Items"):
                return self.slot2Items
        elif slot == 3:
            if hasattr(self, "slot3Items"):
                return self.slot3Items
        elif slot == 4:
            if hasattr(self, "slot4Items"):
                return self.slot4Items
        elif slot == 5:
            if hasattr(self, "slot5Items"):
                return self.slot5Items
        else:
            return None








    def setItems(self, slot, items):
        if slot == 0:
            self.slot0Items = items
        elif slot == 1:
            self.slot1Items = items
        elif slot == 2:
            self.slot2Items = items
        elif slot == 3:
            self.slot3Items = items
        elif slot == 4:
            self.slot4Items = items
        elif slot == 5:
            self.slot5Items = items

    def d_setItems(self, slot, items):
        items = self.checkItems(items)
        if slot == 0:
            self.sendUpdate("setSlot0Items", [items])
        elif slot == 1:
            self.sendUpdate("setSlot1Items", [items])
        elif slot == 2:
            self.sendUpdate("setSlot2Items", [items])
        elif slot == 3:
            self.sendUpdate("setSlot3Items", [items])
        elif slot == 4:
            self.sendUpdate("setSlot4Items", [items])
        elif slot == 5:
            self.sendUpdate("setSlot5Items", [items])




    def b_setItems(self, slot, items):
        items = self.checkItems(items)
        self.setItems(slot, items)
        self.d_setItems(slot, items)

    def setSlot0ToonId(self, avId):
        self.slot0ToonId = avId

    def setSlot1ToonId(self, avId):
        self.slot1ToonId = avId

    def setSlot2ToonId(self, avId):
        self.slot2ToonId = avId

    def setSlot3ToonId(self, avId):
        self.slot3ToonId = avId

    def setSlot4ToonId(self, avId):
        self.slot4ToonId = avId

    def setSlot5ToonId(self, avId):
        self.slot5ToonId = avId

    def setSlot0Items(self, items):
        self.slot0Items = items

    def setSlot1Items(self, items):
        self.slot1Items = items

    def setSlot2Items(self, items):
        self.slot2Items = items

    def setSlot3Items(self, items):
        self.slot3Items = items

    def setSlot4Items(self, items):
        self.slot4Items = items

    def setSlot5Items(self, items):
        self.slot5Items = items


    def getSlot0ToonId(self):
        if hasattr(self, "slot0ToonId"):
            return self.slot0ToonId
        else:
            return 0

    def getSlot1ToonId(self):
        if hasattr(self, "slot1ToonId"):
            return self.slot1ToonId
        else:
            return 0

    def getSlot2ToonId(self):
        if hasattr(self, "slot2ToonId"):
            return self.slot2ToonId
        else:
            return 0

    def getSlot3ToonId(self):
        if hasattr(self, "slot3ToonId"):
            return self.slot3ToonId
        else:
            return 0

    def getSlot4ToonId(self):
        if hasattr(self, "slot4ToonId"):
            return self.slot4ToonId
        else:
            return 0

    def getSlot5ToonId(self):
        if hasattr(self, "slot5ToonId"):
            return self.slot5ToonId
        else:
            return 0

    def getSlot0Items(self):
        if hasattr(self, "slot0Items"):
            return self.slot0Items
        else:
            return []

    def getSlot1Items(self):
        if hasattr(self, "slot1Items"):
            return self.slot1Items
        else:
            return []

    def getSlot2Items(self):
        if hasattr(self, "slot2Items"):
            return self.slot2Items
        else:
            return []

    def getSlot3Items(self):
        if hasattr(self, "slot3Items"):
            return self.slot3Items
        else:
            return []

    def getSlot4Items(self):
        if hasattr(self, "slot4Items"):
            return self.slot4Items
        else:
            return []

    def getSlot5Items(self):
        if hasattr(self, "slot5Items"):
            return self.slot5Items
        else:
            return []

    def getLastEpochTimeStamp(self):
        return self.lastEpochTimeStamp

    def setLastEpochTimeStamp(self, ts):
        self.lastEpochTimeStamp = ts

    def saveTime(self):
        currentTime = time.time()
        self.setLastEpochTimeStamp(currentTime)
        self.sendUpdate("setLastEpochTimeStamp", [currentTime])

   
     
    def setClouds(self, clouds):
        self.clouds = clouds

    def getClouds(self):
        if hasattr(self, "clouds"):
            return self.clouds
        else:
            return 0

    def d_setClouds(self, clouds):
        self.sendUpdate("setClouds", [clouds])

    def b_setClouds(self, clouds):
        self.setClouds(clouds)
        self.d_setClouds(clouds)

    def setRentalTimeStamp(self, rentalTimeStamp):
        self.rentalTimeStamp = rentalTimeStamp

    def getRentalTimeStamp(self):
        if hasattr(self, "rentalTimeStamp"):
            return self.rentalTimeStamp
        else:
            self.rentalTimeStamp = 0
            return 0

    def d_setRentalTimeStamp(self, rentalTimeStamp):
        self.sendUpdate("setRentalTimeStamp", [rentalTimeStamp])

    def b_setRentalTimeStamp(self, rentalTimeStamp):
        self.setRentalTimeStamp(rentalTimeStamp)
        self.d_setRentalTimeStamp(rentalTimeStamp)


    def setRentalType(self, rentalType):
        self.rentalType = rentalType

    def getRentalType(self):
        if hasattr(self, "rentalType"):
            return self.rentalType
        else:
            self.rentalType = 0
            return 0

    def d_setRentalType(self, rentalType):
        self.sendUpdate("setRentalType", [rentalType])

    def b_setRentalType(self, rentalType):
        self.setRentalType(rentalType)
        self.d_setRentalType(rentalType)

    def giveCannonTime(self, seconds):
        timeleft = 0
        if self.rentalType == ToontownGlobals.RentalCannon:
            timeleft = self.rentalTimeStamp - currentTime
            if timeleft < 0:
                timeleft = 0
        currentTime = time.time()
        newTime = currentTime + seconds + timeleft
        self.b_setRentalTimeStamp(newTime)
        self.makeCannonsUntil(newTime)


    def makeCannonsUntil(self, endTime):
        #print("makeing cannons until")
        self.startCannons()
        currentTime = time.time()
        secondsUntil = endTime - currentTime
        taskMgr.remove(self.uniqueName("endCannons"))
        taskMgr.doMethodLater(secondsUntil, self.endCannons, self.uniqueName("endCannons"))
        taskMgr.remove(self.uniqueName("endCannonsNotify"))
        taskMgr.doMethodLater(secondsUntil, self.notifyCannonsEnd, self.uniqueName("endCannonsNotify"))

    def makeGameTableUntil(self, endTime):
        self.notify.info('making game table until')
        self.startGameTable()
        currentTime = time.time()
        secondsUntil = endTime - currentTime
        taskMgr.remove(self.uniqueName("endGameTable"))
        taskMgr.doMethodLater(secondsUntil, self.endGameTable, self.uniqueName("endGameTable"))
        
    def startGameTable(self, avatar = 0):
        if self.gameTableFlag:
            return        
        if not self.picnicTable:
            self.notify.info('creating game table')
            # Create the game table
            pos = Point3(55, -20, 8.8)
            hpr = Point3(0, 0, 0)
            self.picnicTable = DistributedPicnicTableAI.DistributedPicnicTableAI(self.air, self.zoneId, 'gameTable',
                                                                                 pos[0], pos[1], pos[2],
                                                                                 hpr[0], hpr[1], hpr[2])
        self.gameTableFlag = True
    
    def endGameTable(self, avatar = 0):
        self.notify.info('endGameTable')
        if not self.gameTableFlag:
            return
        if self.picnicTable:
            # delete the game table
            self.picnicTable.requestDelete()
            del self.picnicTable
            self.picnicTable = None
            
        # Tell the client that the game table rental is over
        self.sendUpdate("gameTableOver", [])
        
        self.gameTableFlag = False
    
    def rentItem(self, type, duration):
        timeleft = 0        
        currentTime = time.time()
        if self.rentalType == type:
            timeleft = self.rentalTimeStamp - currentTime
            if timeleft < 0:
                timeleft = 0
        newTime = currentTime + (duration * 60) + timeleft
        self.air.writeServerEvent('rental', self.doId, "New rental end time %s." % (newTime))
        
        self.b_setRentalTimeStamp(newTime)
        self.b_setRentalType(type)
        if type == ToontownGlobals.RentalCannon:
            self.makeCannonsUntil(newTime)
        elif type == ToontownGlobals.RentalGameTable:
            self.makeGameTableUntil(newTime)


