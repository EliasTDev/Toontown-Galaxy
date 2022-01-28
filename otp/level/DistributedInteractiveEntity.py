""" DistributedInteractiveEntity module: contains the DistributedInteractiveEntity
    class, the client side representation of a 'landmark door'."""

from pandac.PandaModules import *
from direct.distributed.ClockDelta import *

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from . import DistributedEntity


class DistributedInteractiveEntity(DistributedEntity.DistributedEntity):
    """
    DistributedInteractiveEntity class:  The client side representation of any
    simple animated prop.
    """

    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedInteractiveEntity')

    def __init__(self, cr):
        """constructor for the DistributedInteractiveEntity"""
        DistributedEntity.DistributedEntity.__init__(self, cr)

        self.fsm = ClassicFSM.ClassicFSM('DistributedInteractiveEntity',
                                         [State.State('off',
                                                      self.enterOff,
                                                      self.exitOff,
                                                      ['playing',
                                                       'attract']),
                                             State.State('attract',
                                                         self.enterAttract,
                                                         self.exitAttract,
                                                         ['playing']),
                                             State.State('playing',
                                                         self.enterPlaying,
                                                         self.exitPlaying,
                                                         ['attract'])],
                                         # Initial State
                                         'off',
                                         # Final State
                                         'off',
                                         )
        self.fsm.enterInitialState()
        # self.generate will be called automatically.

    def generate(self):
        """
        This method is called when the DistributedEntity is introduced
        to the world, either for the first time or from the cache.
        """
        DistributedEntity.DistributedEntity.generate(self)

    def disable(self):
        # Go to the off state when the object is put in the cache
        self.fsm.request("off")
        DistributedEntity.DistributedEntity.disable(self)
        # self.delete() will automatically be called.

    def delete(self):
        del self.fsm
        DistributedEntity.DistributedEntity.delete(self)

    def setAvatarInteract(self, avatarId):
        """
        required dc field.
        """
        assert avatarId not in self.__dict__
        self.avatarId = avatarId

    def setOwnerDoId(self, ownerDoId):
        """
        required dc field.
        """
        assert "ownerDoId" not in self.__dict__
        self.ownerDoId = ownerDoId

    def setState(self, state, timestamp):
        if self.isGenerated():
            self.fsm.request(
                state, [
                    globalClockDelta.localElapsedTime(timestamp)])
        else:
            self.initialState = state
            self.initialStateTimestamp = timestamp

    # def __getPropNodePath(self):
    #    #("__getPropNodePath()")
    #    if (not self.__dict__.has_key('propNodePath')):
    #        self.propNodePath=self.cr.playGame.hood.loader.geom.find(
    #                "**/prop"+self.entID+":*_DNARoot")
    #    return self.propNodePath

    def enterTrigger(self, args=None):
        # ("enterTrigger(args="+str(args)+")")
        messenger.send("DistributedInteractiveEntity_enterTrigger")
        self.sendUpdate("requestInteract")
        # the AI server will reply with toonInteract or rejectInteract.

    def exitTrigger(self, args=None):
        # ("exitTrigger(args="+str(args)+")")
        messenger.send("DistributedInteractiveEntity_exitTrigger")
        self.sendUpdate("requestExit")
        # the AI server will reply with avatarExit.

    def rejectInteract(self):
        """
        Server doesn't let the avatar interact with prop.
        """
        # ("rejectInteract()")
        self.cr.playGame.getPlace().setState('walk')

    def avatarExit(self, avatarId):
        return
        # ("avatarExit(avatarId=%s)"%(avatarId,))

    ##### off state #####

    def enterOff(self):
        return
        # ("enterOff()")

    def exitOff(self):
        return
        # ("exitOff()")

    ##### attract state #####

    def enterAttract(self, ts):
        return
        # ("enterAttract()")

    def exitAttract(self):
        return
        # ("exitAttract()")

    ##### playing state #####

    def enterPlaying(self, ts):
        return
        # ("enterPlaying()")

    def exitPlaying(self):
        return
        # ("exitPlaying()")
