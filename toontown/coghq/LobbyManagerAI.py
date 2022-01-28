from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals


class LobbyManagerAI(DistributedObjectAI.DistributedObjectAI):

    notify = DirectNotifyGlobal.directNotify.newCategory('LobbyManagerAI')

    def __init__(self, air, bossConstructor):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.air = air
        self.bossConstructor = bossConstructor

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.notify.debug('generate')

    def delete(self):
        self.notify.debug("delete")
        self.ignoreAll()
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def createBossOffice(self, avIdList):
        bossZone = self.air.allocateZone()
        self.notify.info(f'createBossOffice: {bossZone}')
        bossCog = self.bossConstructor(self.air)
        #bossCog = DistributedSellbotBossAI.DistributedSellbotBossAI(self.air)
        bossCog.generateWithRequired(bossZone)
        self.acceptOnce(bossCog.uniqueName('BossDone'),
                        self.destroyBossOffice, extraArgs=[bossCog])

        # Tell the boss about the toons coming.
        for avId in avIdList:
            if avId:
                bossCog.addToon(avId)

        bossCog.b_setState('WaitForToons')
        return bossZone

    def destroyBossOffice(self, bossCog):
        bossZone = bossCog.zoneId
        self.notify.info(f'destroyBossOffice: {bossZone}')
        bossCog.requestDelete()
        self.air.deallocateZone(bossZone)
