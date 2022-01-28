from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import random
from toontown.suit import SuitDNA
from . import CogDisguiseGlobals
from toontown.toonbase.ToontownBattleGlobals import getInvasionMultiplier
from functools import reduce

MeritMultiplier = 2.0


class PromotionManagerAI:

    notify = DirectNotifyGlobal.directNotify.newCategory("PromotionManagerAI")

    def __init__(self, air):
        self.air = air

    def getPercentChance(self):
        # todo: make this interesting
        return 100.0

    def recoverMerits(
            self,
            av,
            cogList,
            zoneId,
            multiplier=1,
            extraMerits=None):
        avId = av.getDoId()
        meritsRecovered = [0, 0, 0, 0]
        if extraMerits is None:
            extraMerits = [0, 0, 0, 0]

        # multiply merit bonus during invasions too
        if self.air.suitInvasionManager.getInvading():
            multiplier *= getInvasionMultiplier()

        # start with any extra merits
        for i in range(len(extraMerits)):
            if CogDisguiseGlobals.isSuitComplete(av.getCogParts(), i):
                meritsRecovered[i] += extraMerits[i]
                self.notify.debug(
                    f"recoverMerits: extra merits = {extraMerits[i]}")

        self.notify.debug(f"recoverMerits: multiplier = {multiplier}")

        # add merits for every cog defeated
        for cogDict in cogList:
            dept = SuitDNA.suitDepts.index(cogDict['track'])
            if avId in cogDict['activeToons']:
                # only let them recover merits if suit is complete
                if CogDisguiseGlobals.isSuitComplete(
                    av.getCogParts(), SuitDNA.suitDepts.index(
                        cogDict['track'])):
                    self.notify.debug(
                        f"recoverMerits: checking against cogDict: {cogDict}")
                    # determine if we 'won' any merits
                    rand = random.random() * 100

                    # don't reward merits for 'virtual' cogs
                    if rand <= self.getPercentChance(
                    ) and not cogDict['isVirtual']:
                        # add in recovered merits
                        merits = cogDict['level'] * MeritMultiplier
                        # round up
                        merits = int(round(merits))
                        # if this cog had revives, reward 2x merits
                        if cogDict['hasRevives']:
                            merits *= 2
                        # add floor/stage bonus
                        merits = merits * multiplier
                        # round up again
                        merits = int(round(merits))
                        # sum it up
                        meritsRecovered[dept] += merits
                        self.notify.debug(
                            f"recoverMerits: merits = {merits}")
                    else:
                        self.notify.debug("recoverMerits: virtual cog!")

        # Now set the merits on the avatar if the status changed
        if meritsRecovered != [0, 0, 0, 0]:
            actualCounted = [0, 0, 0, 0]
            merits = av.getCogMerits()
            for i in range(len(meritsRecovered)):
                max = CogDisguiseGlobals.getTotalMerits(av, i)
                if max:
                    # if we are under level max, inc merits
                    if merits[i] + meritsRecovered[i] <= max:
                        actualCounted[i] = meritsRecovered[i]
                        merits[i] += meritsRecovered[i]
                    else:
                        actualCounted[i] = max - merits[i]
                        # otherwise set to max
                        merits[i] = max
                    # update the toons merits
                    av.b_setCogMerits(merits)

            # Only log if they actually got some merits
            if reduce(lambda x, y: x + y, actualCounted):
                self.air.writeServerEvent(
                    'merits', avId, ("%s|%s|%s|%s" %
                                     tuple(actualCounted)))
                self.notify.debug(
                    f"recoverMerits: av {avId} recovered merits {actualCounted}")

        return meritsRecovered
