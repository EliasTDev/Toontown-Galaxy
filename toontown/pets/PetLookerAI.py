# PetLookerAI

from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from otp.ai.AIZoneData import AIZoneData
from toontown.toonbase import ToontownGlobals
from toontown.pets import PetConstants

# TODO: add a check to determine if you're really facing the pet?

# these events deal with avIds so that we can generate events for avatars
# that are not (any longer) instantiated

# these events are generated when an avatar (avId) starts looking at another
# avatar. avId of other avatar should be passed as event argument


def getStartLookingAtOtherEvent(lookingAvId):
    return f'PetLookerAI-{lookingAvId}-startLookingAtOther'


def getStopLookingAtOtherEvent(lookingAvId):
    return f'PetLookerAI-{lookingAvId}-stopLookingAtOther'
# these events are generated when an avatar (avId) starts being looked at
# by another avatar. avId of other avatar should be passed as event argument


def getStartLookedAtByOtherEvent(lookedAtAvId):
    return f'PetLookerAI-{lookedAtAvId}-startLookedAtByOther'


def getStopLookedAtByOtherEvent(lookedAtAvId):
    return f'PetLookerAI-{lookedAtAvId}-stopLookedAtByOther'


class PetLookerAI:
    """mixin class for distributed avatars that can be looking at a pet,
    and also can be looked at by a pet.

    Master obj must:
     - inherit from DistributedObjectAI
     - if obj is a pet, override _isPet to return non-zero
     - call __init__ on construction and call destroy() on deletion
     - call enterPetLook() when it is near pets
     - call exitPetLook() when it is no longer near pets
    """

    notify = DirectNotifyGlobal.directNotify.newCategory('PetLookerAI')

    def __init__(self):
        self.__active = 0
        self.others = {}

    def destroy(self):
        if self.__active:
            self.exitPetLook()
        if len(self.others):
            PetLookerAI.notify.warning('%s: self.others not empty: %s' %
                                       (self.doId, list(self.others.keys())))
            self.others = {}

    def _getPetLookerBodyNode(self):
        # if the avatar is not a node, override this and return the avatar's
        # body node
        return self

    def _isPet(self):
        return 0

    def enterPetLook(self):
        PetLookerAI.notify.debug(f'enterPetLook: {self.doId}')
        if self.__active:
            PetLookerAI.notify.warning(f"enterPetLook: {self.doId} already active!")
            return
        if len(self.others):
            PetLookerAI.notify.warning("%s: len(self.others) != 0: %s" %
                                       (self.doId, list(self.others.keys())))
            self.others = {}

        self.__active = 1
        self.__collNode = self._getPetLookerBodyNode().attachNewNode(
            'PetLookerCollNode')
        self._createPetLookSphere()

    def exitPetLook(self):
        PetLookerAI.notify.debug(f'exitPetLook: {self.doId}')
        if not self.__active:
            PetLookerAI.notify.warning(f'exitPetLook: {self.doId} not active!')
            return

        # if we're still showing as looking at someone, force not looking.
        # this is a hack, we shouldn't have to do this.
        if len(self.others):
            otherIds = list(self.others.keys())
            PetLookerAI.notify.warning(f'{self.doId}: still in otherIds: {otherIds}')
            for otherId in otherIds:
                self._handleLookingAtOtherStop(otherId)

            if len(self.others):
                PetLookerAI.notify.warning(
                    "%s: self.others still not empty: %s" %
                    (self.doId, list(self.others.keys())))
                self.others = {}

        self._destroyPetLookSphere()
        self.__collNode.removeNode()
        del self.__collNode
        self.__active = 0

    def _createPetLookSphere(self):
        # creates a sphere that will collide with PetLookerAI probe segments
        # to detect when another PetLooker is looking at us
        isPet = self._isPet()
        if isPet:
            radius = PetConstants.PetSphereRadius
        else:
            radius = PetConstants.NonPetSphereRadius
        lookSphere = CollisionSphere(0, 0, 0, radius)
        lookSphereNode = CollisionNode(f'petLookSphere-{self.doId}')
        lookSphereNode.addSolid(lookSphere)
        lookSphereNode.setFromCollideMask(BitMask32.allOff())
        # this sphere represents us in the collision graph, and collides
        # against other avatars' spheres. Everyone collides with pets,
        # nobody collides with non-pets
        if isPet:
            intoCollideMask = ToontownGlobals.PetLookatPetBitmask
            # if we are a pet, we want to collide with pets and non-pets
            fromCollideMask = (ToontownGlobals.PetLookatPetBitmask |
                               ToontownGlobals.PetLookatNonPetBitmask)
        else:
            intoCollideMask = ToontownGlobals.PetLookatNonPetBitmask
            # non-pets only collide with pets
            fromCollideMask = ToontownGlobals.PetLookatPetBitmask
        lookSphereNode.setIntoCollideMask(intoCollideMask)
        lookSphereNode.setFromCollideMask(fromCollideMask)
        self.lookSphereNodePath = (
            self.__collNode.attachNewNode(lookSphereNode))
        # include a reference to ourself on the node so that colliders
        # know who they collided with. I'd like to just set a python reference
        # here, but that doesn't make it through to the collision handler.
        # Use node tags instead (dict of string->string)
        self.lookSphereNodePath.setTag('petLooker', f'{self.doId}')

        # set up the collision event generation and handling
        self._cHandler = CollisionHandlerEvent()
        self._cHandler.addInPattern(self._getLookingStartEvent())
        self._cHandler.addOutPattern(self._getLookingStopEvent())

        # getCollTrav is a DistObjAI func. We must be in the right zone before
        # calling this.
        collTrav = self.getCollTrav()
        if collTrav:
            collTrav.addCollider(self.lookSphereNodePath, self._cHandler)

        self.accept(self._getLookingStartEvent(),
                    self._handleLookingAtOtherStart)
        self.accept(self._getLookingStopEvent(),
                    self._handleLookingAtOtherStop)

        # don't override any existing self.accept(self.getZoneChangeEvent())
        # handlers; use a proxy obj
        if hasattr(self, 'eventProxy'):
            PetLookerAI.notify.warning(f'{self.doId}: already have an eventProxy!')
        else:
            self.eventProxy = DirectObject.DirectObject()
            self.eventProxy.accept(self.getZoneChangeEvent(),
                                   self._handleZoneChange)

    def _destroyPetLookSphere(self):
        collTrav = self.getCollTrav()
        if collTrav:
            collTrav.removeCollider(self.lookSphereNodePath)
        del self._cHandler
        self.lookSphereNodePath.removeNode()
        del self.lookSphereNodePath
        self.ignore(self._getLookingStartEvent())
        self.ignore(self._getLookingStopEvent())
        self.eventProxy.ignoreAll()
        del self.eventProxy

    def _handleZoneChange(self, newZoneId, oldZoneId):
        PetLookerAI.notify.debug(f'_handleZoneChange: {self.doId}')
        if not self.__active:
            PetLookerAI.notify.warning(
                f'{self.doId}: _handleZoneChange: not active!')
            return
        # remove ourselves from the old collision traverser
        oldZoneData = AIZoneData(self.air, self.parentId, oldZoneId)
        if oldZoneData.hasCollTrav():
            oldZoneData.getCollTrav().removeCollider(self.lookSphereNodePath)
        oldZoneData.destroy()
        # and add to the new
        newZoneData = AIZoneData(self.air, self.parentId, newZoneId)
        if newZoneData.hasCollTrav():
            newZoneData.getCollTrav().addCollider(self.lookSphereNodePath, self._cHandler)
        newZoneData.destroy()

    def _getLookingStartEvent(self):
        return f'PetLookerAI-lookingStart-{self.doId}'

    def _getLookingStopEvent(self):
        return f'PetLookerAI-lookingStop-{self.doId}'

    def __getOtherLookerDoIdFromCollEntry(self, collEntry):
        # figure out what PetLooker we collided with from the collision entry
        into = collEntry.getIntoNodePath()
        if not into.hasTag('petLooker'):
            return 0
        return int(into.getTag('petLooker'))

    def _handleLookingAtOtherStart(self, other):
        if not self.__active:
            PetLookerAI.notify.warning(
                f'{self.doId}: _handleLookingAtOtherStart: not active!')
            return

        # we have started looking at this other PetLooker
        if isinstance(other, CollisionEntry):
            other = self.__getOtherLookerDoIdFromCollEntry(other)
            if other == 0:
                PetLookerAI.notify.warning(
                    f'{self.doId}: looking at unknown other avatar')
                return

        PetLookerAI.notify.debug(
            f'_handleLookingAtOtherStart: {self.doId} looking at {other}')

        if (other in self.others):
            PetLookerAI.notify.warning(
                f"{self.doId}: other ({other}) is already in self.others!")
            if not hasattr(self, "_cHandler"):
                PetLookerAI.notify.warning(
                    "-->The looker sphere has already been destroyed")
        else:
            self.others[other] = None
            messenger.send(getStartLookingAtOtherEvent(self.doId), [other])
            messenger.send(getStartLookedAtByOtherEvent(other), [self.doId])

    def _handleLookingAtOtherStop(self, other):
        if not self.__active:
            PetLookerAI.notify.warning(
                f'{self.doId}: _handleLookingAtOtherStop: not active!')
            return

        # we have stopped looking at this other PetLooker
        if isinstance(other, CollisionEntry):
            other = self.__getOtherLookerDoIdFromCollEntry(other)
            if other == 0:
                PetLookerAI.notify.warning(
                    f'{self.doId}: stopped looking at unknown other avatar')
                return

        PetLookerAI.notify.debug(
            f'_handleLookingAtOtherStop: {self.doId} no longer looking at {other}')

        if (other not in self.others):
            PetLookerAI.notify.warning(
                f"{self.doId}: other ({other}) is not in self.others!")
            if not hasattr(self, "_cHandler"):
                PetLookerAI.notify.warning(
                    "-->The looker sphere has already been destroyed")
        else:
            del self.others[other]
            messenger.send(getStopLookingAtOtherEvent(self.doId), [other])
            messenger.send(getStopLookedAtByOtherEvent(other), [self.doId])
