from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class CentralLoggerUD(DistributedObjectGlobalUD):
    def sendMessage(self, category, description, sender, receiver):
        self.air.writeServerEvent(category, sender, receiver, description)