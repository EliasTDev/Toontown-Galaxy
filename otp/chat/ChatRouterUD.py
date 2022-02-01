from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from toontown.chat.TTWhiteList import TTWhiteList
from discord_webhook import DiscordWebhook, DiscordEmbed

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
        acId = self.air.getAccountIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(), 'Account sent chat without an avatar')
            return
        channel = avId

        mods = self.filterWhitelist(message)

        do = self.air.dclassesByName['DistributedPlayerUD']
        args = [avId, 0, '', message, mods, 0]
        datagram = do.aiFormatUpdate('setTalk', avId, channel, self.air.ourChannel, args)
        self.air.send(datagram)
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/937991478951690320/qYM7lrA82N0Fom1jheSlyWReQjUZB_KaDLgBF7DfmFkwECV3uQ6JhrBfve5yLP_KYd6s', rate_limit_retry=True)
        embed = DiscordEmbed(title='Chat Log')
        # TODO make this an ai function so we can grab the toon's name
        embed.add_embed_field(name='Avatar id: ', value=avId)
        embed.add_embed_field(name='Account id: ', value=acId)
        embed.add_embed_field(name='Message: ', value=message)
        webhook.add_embed(embed)
        response = webhook.execute()

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
