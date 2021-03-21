## """
## """

## from direct.distributed.ClockDelta import *

## from direct.directnotify import DirectNotifyGlobal
## from direct.distributed import DistributedObject

## class DistributedGuildMembership(DistributedObject.DistributedObject):
    ## """
    ## See Also:
        ## "otp/src/configfiles/otp.dc"
        ## "otp/src/guild/DistributedGuildMembershipAI.py"
    ## """

    ## def __init__(self, air):
        ## assert self.notify.debugCall()
        ## DistributedObject.DistributedObject.__init__(self, air)

    ## def delete(self):
        ## assert self.notify.debugCall()
        ## self.ignoreAll()
        ## DistributedObject.DistributedObject.delete(self)
