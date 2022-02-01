from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal

class ChatRouter(DistributedObjectGlobal):
    notify = directNotify.newCategory('ChatRouter')

    def sendChatMessage(self, message):
        self.sendNearbyToons()
        taskMgr.doMethodLater(0.01, self.__sendActualChatMessage, 'chatMessage', extraArgs=[message])

    def __sendActualChatMessage(self, message):
        self.sendUpdate('chatMessage',
            [message])
        
    def sendWhisperMessage(self, message, receiverAvId):
        self.sendUpdate('whisperMessage', [message, receiverAvId])
        
    def sendNearbyToons(self):
        """
        Send nearby player ids to the ai
        """
        nearbyPlayers = base.localAvatar.getNearbyPlayers()
        self.sendUpdate('nearby_toons_command', [nearbyPlayers])
