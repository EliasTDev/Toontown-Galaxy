from . import UtilityStart
import time
from . import DatabaseObject
from . import RepairAvatars


class game:
    name = "toontown"
    process = "ai"


__builtins__["game"] = game()


class NPCFriendsFixer(RepairAvatars.AvatarIterator):
    # When we come to this many non-avatars in a row, assume we have
    # reached the end of the database.
    endOfListCount = 2000

    def fieldsToGet(self, db):
        return ['setName', 'setMoney', 'setMaxNPCFriends']

    def processAvatar(self, av, db):
        self.printSometimes(av)
        if hasattr(av, "maxNPCFriends") and av.maxNPCFriends < 8:
            print(f"Fixing {av.doId}: {av._name}")
            av.b_setMaxNPCFriends(8)
            db2 = DatabaseObject.DatabaseObject(self.air, av.doId)
            db2.storeObject(av, ['setMaxNPCFriends'])
        return

    def printSometimes(self, av):
        now = time.time()
        if now - self.lastPrintTime > self.printInterval:
            print("Avatar %d: %s" % (av.doId, av._name))
            self.lastPrintTime = now


f = NPCFriendsFixer(simbase.air)
f.start()
run()
