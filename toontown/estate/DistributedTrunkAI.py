from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.ai.AIBaseGlobal import *
from panda3d.core import *
from direct.fsm import ClassicFSM
from direct.distributed import ClockDelta
from . import DistributedFurnitureItemAI
from direct.task.Task import Task
from direct.fsm import State
from toontown.estate import DistributedClosetAI
from . import ClosetGlobals
from toontown.toon import ToonDNA
from toontown.toon import DistributedToonAI
class DistributedTrunkAI(DistributedClosetAI.DistributedClosetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrunkAI')


    def __init__(self, air, furnitureMgr, catalogItem):
        DistributedClosetAI.DistributedClosetAI.__init__(self, air, furnitureMgr, catalogItem)
        self.hatList = []
        self.glassesList = []
        self.backpackList = []
        self.shoesList = []
        self.deletedAccessories = []
        self.busy = 0
        self.ownerId = self.furnitureMgr.house.ownerId
        self.ownerAv = None
        self.timedOut = 0
        self.dummyToonAI = None #in case we open a closet of someone not online, keep track of it

    def delete(self):
        self.notify.debug("delete()")
        self.ignoreAll()
        self.customerDNA = None
        self.customerId = None
        del self.deletedAccessories
        taskMgr.remove(self.uniqueName('clearMovie'))
        DistributedClosetAI.DistributedClosetAI.delete(self)

    def freeAvatar(self, avId):
        self.notify.debug("freeAvatar %d" % avId)
        # Free this avatar, probably because he requested interaction while
        # I was busy. This can happen when two avatars request interaction
        # at the same time. The AI will accept the first, sending a setMovie,
        # and free the second
        self.sendUpdateToAvatarId(avId, "freeAvatar", [])

    def enterAvatar(self):
        self.notify.debug("enterAvatar")
        # this avatar has come within range
        avId = self.air.getAvatarIdFromSender()
        # If the closet is already being used, free this avatar

        if self.busy > 0:
            self.freeAvatar(avId)
            return
        # Store the original customer DNA so we can revert if a disconnect
        # happens
        av = self.air.doId2do.get(avId)
        if not av:
            return #something has gone horridly wrong lets not crash the ai

        self.customerDNA = ToonDNA.ToonDNA()
        self.customerDNA.makeFromNetString(av.getDNAString())
        self.customerId = avId
        self.busy = avId
        # Handle unexpected exit
        self.acceptOnce(self.air.getAvatarExitEvent(avId),
                        self.__handleUnexpectedExit, extraArgs=[avId])
        self.acceptOnce("bootAvFromEstate-"+str(avId),
                        self.__handleBootMessage, extraArgs=[avId])

        if self.ownerId:
            self.ownerAv = None
            if self.ownerId in self.air.doId2do:
                self.ownerAv = self.air.doId2do[self.ownerId]
                self.__openTrunk()
            else:
                self.air.dbInterface.queryObject(self.air.dbId, self.ownerId, self.__handleOwnerQuery,
                                             self.air.dclassesByName['DistributedToonAI'])
        else:
            self.notify.warning("this house has no owner, therefore we can't use the closet")
            # send a reset message to the client.  same as a completed purchase
            self.completePurchase(avId)

        self.sendUpdate('setState', [ClosetGlobals.OPEN, avId, self.ownerId, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList])




        self.sendUpdate('setState', [ClosetGlobals.OPEN, avId, self.ownerId, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList])

        # Add a 200 second timeout that'll kick the avatar out:
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.sendTimeoutMovie,  self.uniqueName('clearMovie'))


    def __openTrunk(self):
        self.notify.debug("__openTrunk")
        if self.ownerAv is not None:
            self.hatList = self.ownerAv.getHatList()
            self.glassesList = self.ownerAv.getGlassesList()
            self.backpackList = self.ownerAv.getBackpackList()
            self.shoesList = self.ownerAv.getShoesList()
        else:
            self.notify.warning('ownerAv is none while trying to open trunk.')
            return
        
        self.sendUpdate("setState", [ClosetGlobals.OPEN,
                                     self.customerId, self.ownerAv.doId,
                                     self.hatList, self.glassesList,
                                     self.backpackList, self.shoesList])
                                    

        # Start the timer
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, 
                              self.sendTimeoutMovie,
                              self.uniqueName('clearMovie'))

    def __handleOwnerQuery(self, dclass, fields):
        self.hatList = fields['setHatList'][0]
        self.glassesList = fields['setGlassesList'][0]
        self.backpackList = fields['setBackpackList'][0]
        self.shoesList = fields['setShoesList'][0]
        style = ToonDNA.ToonDNA()
        style.makeFromNetString(fields['setDNAString'][0])

        self.sendUpdate('setMovie', [ClosetGlobals.CLOSET_MOVIE_CLEAR, self.customerId, ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendUpdate('setState', [ClosetGlobals.OPEN, self.customerId, self.ownerId, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList])

        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.__handleClosetTimeout,
                              'closet-timeout-%d' % self.customerId, extraArgs=[self.customerId])


    def removeItem(self, idx, textureIdx, colorIdx, which):
        if not av:
            return
        if self.ownerId != self.avId:
            self.air.writeServerEvent('suspicious', avId, "Toon tried to delete an accessory that wasn't theirs.")
            return
        if self.getLocation != av.getLocation():
            self.air.writeServerEvent('suspicious', avId, "Toon tried to delete an accessory when they aren't in the same zone as the trunk.")
            return 



        # make a list of things to be deleted later, when user is "finished"
        if which:
            self.deletedHats.append((which, idx, textureIdx, colorIdx))



    def setDNA(self, blob, finished, which):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.customerId:
            if self.customerId:
                self.air.writeServerEvent('suspicious', avId, 'DistributedTrunkAI.setDNA current customer %s' % (self.customerId))
                self.notify.warning("customerId: %s, but got setDNA for: %s" % (self.customerId, avId))
            return
        if (avId in self.air.doId2do):
            av = self.air.doId2do[avId]
            testDNA = ToonDNA.ToonDNA()
            if not testDNA.isValidNetString(blob):
                self.air.writeServerEvent('suspicious', avId, 'DistributedTrunkAI.setDNA: invalid dna: %s' % blob)
                return
            if finished == 0:
                #TODO security check here
                #make sure they are only changing accessories here with client
                self.sendUpdate("setCustomerDNA", [avId, blob])

                return

            elif finished == 1:
                av.b_setDNAString(self.customerDNA.makeNetString())
                self.customerId = 0
                self.customerDNA = None
                self.deletedGlasses = []
                self.deletedHats = []
                self.deletedBackpacks = []
                self.deletedShoes = []
                self.hatList = []
                self.glassesList = []
                self.backpackList = []
                self.shoesList = []

            elif finished == 2:

                if self.ownerId != avId:
                    self.air.writeServerEvent('suspicious', avId,
                                              'Toon tried to take accessories that are not theirs.')
                    return
                newDNA = self.updateToonAccessories(av, blob)
                hat = (newDNA.hatModel, newDNA.hatTex, newDNA.hatColor)
                glasses = (newDNA.glassesModel, newDNA.glassesTex, newDNA.glassesColor)
                backpack = (newDNA.backpackModel, newDNA.backpackTex, newDNA.backpackColor)
                shoes = (newDNA.shoesModel, newDNA.shoesTex, newDNA.shoesColor)
                accessories = (hat, glasses, backpack, shoes)

                types = (ToonDNA.HAT, ToonDNA.GLASSES, ToonDNA.BACKPACK, ToonDNA.SHOES)
                for i, accessory in enumerate(accessories):
                    if not av.checkAccessorySanity(types[i], *accessory):
                        # TODO do something better here then just returning 
                        return
                if which & ToonDNA.HAT:
                    if av.replaceItemInAccessoriesList(newDNA.hatModel,
                                                       newDNA.hatTex,
                                                       newDNA.hatColor,
                                                       self.customerDNA.hatModel,
                                                       self.customerDNA.hatTex,
                                                       self.customerDNA.hatColor
                                                       ):
                        av.b_setHat(av.getHatList())
                    else:
                        self.notify.warning('Trunk: setDNA() - unable to save old hats - we exceeded the hats list length')


                if which & ToonDNA.GLASSES:
                    if av.replaceItemInAccessoriesList(newDNA.glassesModel,
                                                       newDNA.glassesTex,
                                                       newDNA.glassesColor,
                                                       self.customerDNA.glassesModel,
                                                       self.customerDNA.glassesTex,
                                                       self.customerDNA.glassesColor):
                        av.b_setGlasses(av.getGlassesList())
                    else:
                        self.notify.warning('Trunk: setDNA() - unable to save old glasses - we exceeded the glasses list length')

                if which & ToonDNA.BACKPACK:
                    if av.replaceItemInAccessoriesList(newDNA.backpackModel,
                                                       newDNA.backpackTex,
                                                       newDNA.backpackColor,
                                                       self.customerDNA.backpackModel,
                                                       self.customerDNA.backpackTex,
                                                       self.customerDNA.backpackColor):
                        av.b_setBackpack(av.getBackpackList())
                    else:
                        self.notify.warning('Trunk: setDNA() - unable to save old backpack - we exceeded the backpack list length')

                if which & ToonDNA.SHOES:
                    if av.replaceItemInAccessoriesList(newDNA.shoesModel,
                                                       newDNA.shoesTex,
                                                       newDNA.shoesColor,
                                                       self.customerDNA.shoesModel,
                                                       self.customerDNA.shoesTex,
                                                       self.customerDNA.shoesColor):
                        av.b_setShoes(av.getShoesList())

                    else:
                        self.notify.warning('Trunk: setDNA() - unable to save old backpack - we exceeded the backpack list length')

                for item in self.deletedAccessories[:]:
                    self.deletedAccessories.remove(item)
                    if not av.removeItemInAccessoriesList(*item):
                        self.air.writeServerEvent('suspicious', avId, 'av tried to delete accessory they don\'t own!')
 
                av.b_setHatList(av.getHatList())
                av.b_setGlassesList(av.getGlassesList())
                av.b_setBackpackList(av.getBackpackList())
                av.b_setShoesList(av.getShoesList())
                self.updateToonAccessories(av, blob)
                self.customerId = 0
                self.customerDNA = None
                self.__finalizeDelete()
                #self.sendUpdate('setMovie', [ClosetGlobals.CLOSET_MOVIE_COMPLETE, avId, ClockDelta.globalClockDelta.getRealNetworkTime()])
                #self.sendUpdate('setMovie', [ClosetGlobals.CLOSET_MOVIE_CLEAR, 0, ClockDelta.globalClockDelta.getRealNetworkTime()])
                #self.sendUpdate('setCustomerDNA', [0 for x in range(14)])
                #self.sendUpdate('setState', [ClosetGlobals.CLOSED, 0, self.ownerId, self.hatList, self.glassesList,
                #            self.backpackList, self.shoesList])
            else:
                self.notify.warning('no av for avId: %d' % avId)
        if (self.timedOut == 1 or finished == 0 or finished == 4):
            return
        if (self.busy == avId):
            self.notify.debug("sending complete purchase movie")
            taskMgr.remove(self.uniqueName('clearMovie'))
            self.completePurchase(avId)
        else:
            self.air.writeServerEvent('suspicious', avId, 'DistributedTrunk.setDNA busy with %s' % (self.busy))
            self.notify.warning('setDNA from unknown avId: %s busy: %s' % (avId, self.busy))
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignore(self.air.getAvatarExitEvent(avId))       



    def updateToonAccessories(self, av, blob):
        proposedDNA = ToonDNA.ToonDNA()
        proposedDNA.makeFromNetString(blob)
        # Don't completely trust the client.  Enforce that only the clothes
        # change here.  This eliminates the possibility of the gender, species, etc
        # of the toon changing, or a bug being exploited.
        updatedDNA = ToonDNA.ToonDNA()
        updatedDNA.makeFromNetString(self.customerDNA.makeNetString())
        updatedDNA.hatModel = proposedDNA.hatModel
        updatedDNA.hatTex = proposedDNA.hatTex
        updatedDNA.hatColor = proposedDNA.hatColor
        updatedDNA.glassesModel = proposedDNA.glassesModel
        updatedDNA.glassesTex = proposedDNA.glassesTex
        updatedDNA.glassesColor = proposedDNA.glassesColor
        updatedDNA.backpackModel = proposedDNA.backpackModel
        updatedDNA.backpackTex = proposedDNA.backpackTex
        updatedDNA.backpackColor = proposedDNA.backpackColor
        updatedDNA.shoesModel = proposedDNA.shoesModel
        updatedDNA.shoesTex = proposedDNA.shoesTex
        updatedDNA.shoesColor = proposedDNA.shoesColor
        av.b_setDNAString(updatedDNA.makeNetString())
        return updatedDNA
        
    def __finalizeDelete(self):
        self.hatList = []
        self.glassesList = []
        self.backpackList = []
        self.shoesList = []
        self.deletedAccessories = []


    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')

        # Only do customer work with the busy id
        if (self.customerId == avId):
            taskMgr.remove(self.uniqueName('clearMovie'))
            toon = self.air.doId2do.get(avId)
            if (toon == None):
                toon = DistributedToonAI.DistributedToonAI(self.air)
                toon.doId = avId

            if self.customerDNA:
                toon.b_setDNAString(self.customerDNA.makeNetString())
                # Force a database write since the toon is gone and might
                # have missed the distributed update.
                #TODO 

        #else:
         #   self.notify.warning('invalid customer avId: %s, customerId: %s ' % (avId, self.customerId))

        # Only do busy work with the busy id
        # Warning: send the clear movie at the end of this transaction because
        # it clears out all the useful values needed here
        if (self.busy == avId):
            self.sendClearMovie(None, avId)
        else:
            self.notify.warning('not busy with avId: %s, busy: %s ' % (avId, self.busy))

    def __handleBootMessage(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' got booted ')
        # Only do customer work with the busy id
        if (self.customerId == avId):
            if self.customerDNA:
                toon = self.air.doId2do.get(avId)
                if toon:
                    toon.b_setDNAString(self.customerDNA.makeNetString())
        self.sendClearMovie(None, avId)
        
        
    def completePurchase(self, avId):
        assert(self.notify.debug('completePurchase()'))
        self.busy = avId
        # Send a movie to reward the avatar
        self.sendUpdate("setMovie", [ClosetGlobals.CLOSET_MOVIE_COMPLETE,
                        avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None, avId)
        return

    def sendTimeoutMovie(self, task):
        assert(self.notify.debug('sendTimeoutMovie()'))
        # The timeout has expired.  Restore the client back to his
        # original DNA automatically (instead of waiting for the
        # client to request this).
        
        toon = self.air.doId2do.get(self.customerId)
        # On second thought, we're better off not asserting this.
        if (toon != None and self.customerDNA):
            toon.b_setDNAString(self.customerDNA.makeNetString())
            # Hmm, suppose the toon has logged out at the same time?
            # Is it possible to miss this update due to a race
            # condition?

        self.timedOut = 1
        self.sendUpdate("setMovie", [ClosetGlobals.CLOSET_MOVIE_TIMEOUT,
                                     self.busy,
                                     ClockDelta.globalClockDelta.getRealNetworkTime()])
        
        self.sendClearMovie(None, self.customerId)
        return Task.done


    def sendClearMovie(self, task, avId):
        assert(self.notify.debug('sendClearMovie()'))
        # Ignore unexpected exits on whoever I was busy with
        self.ignoreAll()
        self.customerDNA = None
        self.customerId = None
        self.busy = 0
        self.timedOut = 0
        self.sendUpdate("setMovie", [ClosetGlobals.CLOSET_MOVIE_CLEAR,
                                     0,
                                     ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendUpdate('setState', [ClosetGlobals.CLOSED, avId, self.ownerId, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList])
        self.sendUpdate("setCustomerDNA", [0, ''])
        #RAU kill mem leak when opening closet that's not yours
        if self.dummyToonAI:
            self.dummyToonAI.deleteDummy()
            self.dummyToonAI = None
        self.ownerAv = None
        return Task.done

    def isClosetOwner(self):
        return self.ownerId == self.customerId

    def getOwnerId(self):
        return self.ownerId
        
