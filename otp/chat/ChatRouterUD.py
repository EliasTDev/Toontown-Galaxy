from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from toontown.chat.TTWhiteList import TTWhiteList

whiteList = TTWhiteList()


class ChatRouterUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ChatRouterUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.extra_whitelisted_words = []

    def filterWhitelist(self, message):
        words = message.split(' ')
        offset = 0
        mods = []

        for word in words:
            if not whiteList.isWord(word) and word not in self.extra_whitelisted_words:
                mods.append((offset, offset + len(word) - 1))

            offset += len(word) + 1

        return mods

    def chatMessage(self, message):
        avId = self.air.getAvatarIdFromSender()

        if not avId:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(), 'Account sent chat without an avatar')
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

    def set_extra_whitelisted_words(self, extra_whitelisted_words):
        self.extra_whitelisted_words = extra_whitelisted_words
        self.notify.debug(f'Extra words: {self.extra_whitelisted_words}')
