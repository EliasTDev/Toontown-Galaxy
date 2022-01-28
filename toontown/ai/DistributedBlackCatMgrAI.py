from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI


class DistributedBlackCatMgrAI(DistributedObjectAI.DistributedObjectAI):
    """This object sits in the tutorial zone with Flippy and listens for
    the avatar to say 'Toontastic!' when prompted to say something. At that
    point, if the avatar is a cat, it gives them the 'black cat' DNA."""
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedBlackCatMgrAI')

    def __init__(self, air, avId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.avId = avId

    def getAvId(self):
        return self.avId

    def doBlackCatTransformation(self):
        avId = self.avId
        if self.air.getAvatarIdFromSender() != avId:
            self.air.writeServerEvent(
                'suspicious', avId, '%s: expected msg from %s, got msg from %s' %
                (self.__class__.__name__, avId, self.air.getAvatarIdFromSender()))
            return

        av = self.air.doId2do.get(self.avId)
        if not av:
            DistributedBlackCatMgrAI.notify.warning(
                f'tried to turn av {avId} into a black cat, but they left')
        else:
            self.air.writeServerEvent(
                'blackCatMade',
                avId,
                f'turning av {avId} into a black cat')
            DistributedBlackCatMgrAI.notify.warning(
                f'turning av {avId} into a black cat')
            av.makeBlackCat()
