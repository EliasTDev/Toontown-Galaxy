from toontown.toonbase.ToonBaseGlobal import *
from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from toontown.dna.DNAParser import *
import ToonInterior
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
import random
import ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.quest import QuestParser
from toontown.toon import DistributedNPCSpecialQuestGiver
from toontown.toonbase import TTLocalizer
from otp.nametag.NametagConstants import CFSpeech


class DistributedTutorialInterior(DistributedObject.DistributedObject):
    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)

        if not base.cr.doFindAllInstances(DistributedNPCSpecialQuestGiver.DistributedNPCSpecialQuestGiver):
            self.acceptOnce('doneTutorialSetup', self.setup)
        else:
            self.setup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        self.street.removeNode()
        del self.street
        self.sky.removeNode()
        del self.sky

        DistributedObject.DistributedObject.disable(self)

    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.randomGenerator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
        return findFunc(code)

    def replaceRandomInModel(self, model):
        baseTag = 'random_'
        npc = model.findAllMatches('**/' + baseTag + '???_*')
        for i in xrange(npc.getNumPaths()):
            np = npc.getPath(i)
            name = np.getName()
            b = len(baseTag)
            category = name[b + 4:]
            key1 = name[b]
            key2 = name[b + 1]
            if key1 == 'm':
                model = self.randomDNAItem(category, self.dnaStore.findNode)
                newNP = model.copyTo(np)
                c = render.findAllMatches('**/collision')
                c.stash()
                if key2 == 'r':
                    self.replaceRandomInModel(newNP)
            elif key1 == 't':
                texture = self.randomDNAItem(category, self.dnaStore.findTexture)
                np.setTexture(texture, 100)
                newNP = np
            if key2 == 'c':
                if category == 'TI_wallpaper' or category == 'TI_wallpaper_border':
                    self.randomGenerator.seed(self.zoneId)
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
                else:
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))

    def setup(self):
        self.dnaStore = base.cr.playGame.dnaStore
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_3.5/models/modules/toon_interior_tutorial')
        self.interior.reparentTo(render)
        dnaStore = DNAStorage()
        node = loader.loadDNAFile(self.cr.playGame.hood.dnaStore, 'phase_3.5/dna/tutorial_street.pdna')
        self.street = render.attachNewNode(node)
        self.street.flattenMedium()
        self.street.setPosHpr(-17, 42, -0.5, 180, 0, 0)
        self.street.find('**/tb2:toon_landmark_TT_A1_DNARoot').stash()
        self.street.find('**/tb1:toon_landmark_hqTT_DNARoot/**/door_flat_0').stash()
        self.street.findAllMatches('**/+CollisionNode').stash()
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(0.8)
        self.sky.reparentTo(render)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        hoodId = ZoneUtil.getCanonicalHoodId(self.zoneId)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.8, 0.8, 0.8)
        door_origin.setPos(door_origin, 0, -0.025, 0)
        color = self.randomGenerator.choice(self.colors['TI_door'])
        setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()
        npcOrigin = self.interior.find('**/npc_origin_' + `(self.cr.doId2do[self.npcId].posIndex)`)
        if not npcOrigin.isEmpty():
            self.cr.doId2do[self.npcId].reparentTo(npcOrigin)
            self.cr.doId2do[self.npcId].clearMat()
        base.localAvatar.setPosHpr(-2, 12, 0, -10, 0, 0)
        self.cr.doId2do[self.npcId].setChatAbsolute(TTLocalizer.QuestScript101_0, CFSpeech)


    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def setTutorialNpcId(self, npcId):
        self.npcId = npcId

    def getTutorialNpc(self):
        return self.cr.doId2do[self.npcId]
