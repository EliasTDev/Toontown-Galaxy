from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify.DirectNotifyGlobal import directNotify


class ChatRouterAI(DistributedObjectGlobalAI):
    notify = directNotify.newCategory('ChatRouterAI')

#TODO implement things like auto warn for blacklist, and chat muting.
    
    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)
        self.air = air

    def nearby_toons_command(self, nearby_player_ids):
        """
        Setups the nearby words for uberdog based on player ids
        given by the client.
        """
        print('Nearby toons command starting')
        nearby_players = []
        extra_whitelisted_words = []
        sender_id = self.air.getAvatarIdFromSender()
        for toon_id in nearby_player_ids:
            try:
                toon = self.air.doId2do.get(toon_id)
                toon_name = str.lower(toon.getName())
                # get the extracted words from the toon name
                extracted_words_toon_name = toon_name.split()
                for word in extracted_words_toon_name:
                    extra_whitelisted_words.append(word)
            except BaseException:
                self.air.writeServerEvent('suspicious',
                                          f'Toon {sender_id}tried sending an invalid toons list {nearby_player_ids}')
                return
        self.notify.debug(extra_whitelisted_words)
        self.sendUpdate('set_extra_whitelisted_words', [extra_whitelisted_words])
