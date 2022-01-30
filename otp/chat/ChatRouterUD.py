from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from toontown.chat.TTWhiteList import TTWhiteList

whiteList = TTWhiteList()

class ChatRouterUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ChatRouterUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.extraWhitelistedWords = []

    def filterWhitelist(self, message):
        words = message.split(' ')
        offset = 0
        mods = []

        for word in words:
            if not whiteList.isWord(word) and not word in self.extraWhitelistedWords:
                mods.append((offset, offset + len(word) - 1))

            offset += len(word) + 1

        return mods

    def chatMessage(self, message):
        avId = self.air.getAvatarIdFromSender()

        if not avId:
            return

        channel = avId

        mods = self.filterWhitelist(message)

        do = self.air.dclassesByName['DistributedPlayerUD']
        args = [avId, 0, '', message, mods, 0]
        datagram = do.aiFormatUpdate('setTalk', avId, channel, self.air.ourChannel, args)
        self.air.send(datagram)

    def whisperMessage(self, message, receiverAvId):
        avId = self.air.getAvatarIdFromSender()

        if not avId:
            return

        mods = self.filterWhitelist(message)

        do = self.air.dclassesByName['DistributedPlayerUD']
        args = [avId, 0, '', message, mods, 0]
        datagram = do.aiFormatUpdate('setTalkWhisper', receiverAvId, receiverAvId, self.air.ourChannel, args)
        self.air.send(datagram)

    def nearbyToonsCommand(self, nearbyPlayerIds):
        self.nearbyPlayers = []
        self.extraWhitelistedWords = []
        senderId = self.air.getAvatarIdFromSender()
        for toonId in nearbyPlayerIds:
            #try:
            toon = self.air.doId2do.get(toonId)
            self.extraWhitelistedWords.append(str.lower(toon.getName()))
            self.extraWhitelistedWords.append(str.title(toon.getName()))
            self.extraWhitelistedWords.append(str.upper(toon.getName()))
        print(self.extraWhitelistedWords)
           # except:
               # self.air.writeServerEvent('suspicious', f'Toon {senderId}tried sending an invalid toons list {nearbyPlayerIds}')

        