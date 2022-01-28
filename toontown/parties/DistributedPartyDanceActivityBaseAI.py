# -------------------------------------------------------------------------------
# Contact: Edmundo Ruiz (Schell Games)
# Created: Oct 2008
#
# Purpose: AI component that manages which toons are currently dancing, who entered
#          and exited the dance floor, and broadcasts dance moves to all clients.
# -------------------------------------------------------------------------------

from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from toontown.parties import PartyGlobals


class DistributedPartyDanceActivityBaseAI(DistributedPartyActivityAI):
    notify = directNotify.newCategory("DistributedPartyDanceActivityBaseAI")

    def __init__(
            self,
            air,
            partyDoId,
            x,
            y,
            h,
            activityId,
            dancePatternToAnims):
        self.notify.debug("Intializing.")
        DistributedPartyActivityAI.__init__(
            self,
            air,
            partyDoId,
            x,
            y,
            h,
            activityId,
            PartyGlobals.ActivityTypes.Continuous)
        self.toonIdsToHeadings = {}  # toon's heading when it joined
        self.dancePatternToAnims = dancePatternToAnims

    def delete(self):
        pass

    # Distributed (clsend airecv)
    def toonJoinRequest(self):
        """Gets from client when a toon enters the dance floor."""
        senderId = self.air.getAvatarIdFromSender()
        self.notify.debug(f"Request enter {senderId}")
        if senderId not in self.toonIds:
            if self.party.isInActivity(senderId):
                hToUse = 0
                toon = self.air.doId2do.get(senderId)
                if toon:
                    hToUse = toon.getH()
                self.sendToonJoinResponse(senderId,
                                          joined=False,
                                          h=hToUse)
            else:
                self.sendToonJoinResponse(senderId,
                                          joined=True,
                                          h=self.air.doId2do[senderId].getH())

        else:
            self.air.writeServerEvent(
                "suspicious",
                senderId,
                "Party Dance Activity AI Join Request: Sender already in Party Dance Activity"
            )
            self.notify.warning(
                "toonJoinRequest() - Sender already in Activity")

    def sendToonJoinResponse(self, toonId, joined=True, h=0.0):
        if joined:
            self._addToon(toonId)
            self.toonIdsToHeadings[toonId] = h
            self.notify.debug("sending setToonsPlaying")
            self.notify.debug(f"    toonIds: {self.toonIds}")
            self.notify.debug(f"    toonHeadings: {self.getHeadingList()}")
            self.sendUpdate(
                "setToonsPlaying", [
                    self.toonIds, self.getHeadingList()])
        else:
            self.sendUpdateToAvatarId(
                toonId, "joinRequestDenied", [
                    PartyGlobals.DenialReasons.SilentFail])

    # Distributed (clsend airecv)
    def toonExitRequest(self):
        """
        Gets from client when a dancing toon enters the dance floor.
        """
        senderId = self.air.getAvatarIdFromSender()
        self.notify.debug(f"Request exit {senderId}")
        if senderId in self.toonIds:
            self.sendToonExitResponse(senderId, exited=True)
        else:
            # this case is possible when a toon lands on dance floor from the cannon
            # joinRequest is never sent by client but exitRequest is sent
            self.sendToonExitResponse(
                senderId,
                exited=False,
                denialReason=PartyGlobals.DenialReasons.SilentFail)

    def sendToonExitResponse(
            self,
            toonId,
            exited,
            denialReason=PartyGlobals.DenialReasons.Default):
        if exited:
            self._removeToon(toonId)
            del self.toonIdsToHeadings[toonId]
            self.sendUpdate(
                "setToonsPlaying", [
                    self.toonIds, self.getHeadingList()])
        else:
            self.sendUpdateToAvatarId(
                toonId, "exitRequestDenied", [denialReason])

    def getHeadingList(self):
        """
        Returns a list of initial headings for toons in the activity, in the
        same order as self.toonIds
        """
        headingList = []
        for toonId in self.toonIds:
            headingList.append(self.toonIdsToHeadings[toonId])
        return headingList

    # Distributed (clsend airecv)
    def updateDancingToon(self, state, anim):
        """
        Gets from client when a dancing toon performs a dance move.
        """
        senderId = self.air.getAvatarIdFromSender()
        if anim != "" and anim not in list(self.dancePatternToAnims.values()):
            # TODO: Log suspicious behavior?
            return
        self.d_setDancingToonState(senderId, state, anim)
        self.notify.debug(f"Request dance move {senderId}")

    # Distributed (broadcast)
    def d_setDancingToonState(self, toonId, state, anim):
        self.sendUpdate("setDancingToonState", [toonId, state, anim])

    def _handleUnexpectedToonExit(self, toonId):
        """
        An avatar bailed out because he lost his connection or quit
        unexpectedly. Overriding base class functionality because of the special
        setToonsPlaying function in this class.
        """
        self._removeToon(toonId)
        self.sendUpdate(
            "setToonsPlaying", [
                self.toonIds, self.getHeadingList()])
