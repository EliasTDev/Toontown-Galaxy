
from otp.ai.AIBaseGlobal import *
from direct.task.Task import Task
from pandac.PandaModules import *
from .DistributedNPCToonBaseAI import *


class DistributedNPCClerkAI(DistributedNPCToonBaseAI):

    def __init__(self, air, npcId):
        DistributedNPCToonBaseAI.__init__(self, air, npcId)
        self.timedOut = 0

    def delete(self):
        taskMgr.remove(self.uniqueName('clearMovie'))
        self.ignoreAll()
        DistributedNPCToonBaseAI.delete(self)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        # this avatar has come within range
        assert self.notify.debug("avatar enter " + str(avId))
        DistributedNPCToonBaseAI.avatarEnter(self)

        # Do what the quest manager does for DistributedNPCToon
        av = self.air.doId2do.get(avId)
        if av is None:
            self.notify.warning(f'toon isnt there! toon: {avId}')
            return

        # Handle unexpected exit
        self.acceptOnce(self.air.getAvatarExitEvent(avId),
                        self.__handleUnexpectedExit, extraArgs=[avId])

        # If NPC is busy, free the avatar
        if (self.isBusy(avId)):
            assert self.notify.debug(
                f'freeing avatar: {avId} because NPCClerk is busy')
            self.freeAvatar(avId)
            return

        if (av.getMoney()):
            self.sendStartMovie(avId)
        else:
            self.sendNoMoneyMovie(avId)

    def sendStartMovie(self, avId):
        avId = self.air.getAvatarIdFromSender()
        assert self.notify.debug('sendStartMovie()')
        if avId not in self.busy:
            self.busy.append(avId)
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_START,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])

        # Timeout
        taskMgr.doMethodLater(NPCToons.CLERK_COUNTDOWN_TIME,
                              self.sendTimeoutMovie,
                              self.uniqueName('clearMovie'))

    def sendNoMoneyMovie(self, avId):
        if avId not in self.busy:
            self.busy.append(avId)
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_NO_MONEY,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return

    def sendTimeoutMovie(self, task):
        avId = self.air.getAvatarIdFromSender()
        assert self.notify.debug('sendTimeoutMovie()')
        self.timedOut = 1
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_TIMEOUT,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return Task.done

    def sendClearMovie(self, task):
        avId = self.air.getAvatarIdFromSender()
        assert self.notify.debug('sendClearMovie()')

        # Ignore unexpected exits on whoever I was busy with
        self.ignore(self.air.getAvatarExitEvent(avId))
        self.busy.remove(avId)
        self.timedOut = 0
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_CLEAR,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        return Task.done

    def completePurchase(self, avId):
        assert self.notify.debug('completePurchase()')
        if avId not in self.busy:
            self.busy.append(avId)
        # Send a movie to reward the avatar
        self.sendUpdate("setMovie", [NPCToons.PURCHASE_MOVIE_COMPLETE,
                        self.npcId, avId,
                        ClockDelta.globalClockDelta.getRealNetworkTime()])
        self.sendClearMovie(None)
        return

    def setInventory(self, blob, newMoney, done):
        assert self.notify.debug(f'setInventory(): {self.timedOut}')
        avId = self.air.getAvatarIdFromSender()

        if avId not in self.busy:
            self.air.writeServerEvent(
                'suspicious',
                avId,
                f'DistributedNPCClerkAI.setInventory busy with {self.busy}')
            self.notify.warning(
                f'setInventory from unknown avId: {avId} busy: {self.busy}')
            return

        if avId in self.air.doId2do:
            av = self.air.doId2do[avId]
            newInventory = av.inventory.makeFromNetString(blob)
            currentMoney = av.getMoney()
            if (av.inventory.validatePurchase(
                    newInventory, currentMoney, newMoney)):
                av.setMoney(newMoney)
                if done:
                    # Tell the state server about the purchase
                    av.d_setInventory(av.inventory.makeNetString())
                    av.d_setMoney(newMoney)
            else:
                self.air.writeServerEvent(
                    'suspicious', avId, 'DistributedNPCClerkAI.setInventory invalid purchase')
                self.notify.warning("Avatar " + str(avId) +
                                    " attempted an invalid purchase.")
                # Make sure the avatar is in sync with the AI.
                av.d_setInventory(av.inventory.makeNetString())
                av.d_setMoney(av.getMoney())

        if self.timedOut:
            return
        if done:
            taskMgr.remove(self.uniqueName('clearMovie'))
            self.completePurchase(avId)

    def __handleUnexpectedExit(self, avId):
        self.notify.warning('avatar:' + str(avId) + ' has exited unexpectedly')
        self.sendTimeoutMovie(None)
        return None
