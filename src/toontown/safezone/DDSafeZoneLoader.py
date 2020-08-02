from toontown.safezone import SafeZoneLoader, DDPlayground
from toontown.toon import NPCToons
from toontown.toonbase import TTLocalizer
import random
from panda3d.core import *
from direct.fsm import State
from direct.interval.IntervalGlobal import *

class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DDPlayground.DDPlayground
        self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/DD_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_DD_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        water = self.geom.find('**/water')
        water.setTransparency(1)
        water.setColor(1, 1, 1, 0.8)
        self.boat = self.geom.find('**/donalds_boat')
        self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')

        if not self.boat.isEmpty():
            wheel = self.boat.find('**/wheel')

            if not wheel.isEmpty():
                wheel.hide()

            self.boat.stash()
            self.donald = NPCToons.createLocalNPC(7011)

            self.donald.setPos(0, -1, 3.95)
            self.donald.reparentTo(self.boat)
            self.donald.setHat(48, 0, 0)
            self.donald.hideShadow()

            random.shuffle(TTLocalizer.DonaldChatter)
            self.donaldSpeech = self.donald.createTalkSequence(TTLocalizer.DonaldChatter, 15)
            self.donaldSpeech.loop(0)

        self.__startWaterEffect()

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)

        if hasattr(self, 'donald'):
         self.donaldSpeech.pause()
         self.donald.delete()
         del self.donaldSpeech
         del self.donald

        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound
        del self.boat
        self.__stopWaterEffect()
        
    def __startWaterEffect(self):
        waterTop = self.geom.find('**/top_surface*')
        waterBottom = self.geom.find('**/bottom_surface*')
        water = self.geom.find('**/water*')
        if not water.isEmpty():
            waterTop.setTexture(loader.loadTexture('phase_4/maps/water3.jpg'), 1)
            waterBottom.setTexture(loader.loadTexture('phase_4/maps/water3.jpg'), 1)
            topE1 = LerpColorScaleInterval(waterTop, 1.5, (.9,.9,.9,1))
            topE2 = LerpColorScaleInterval(waterTop, 1.5, (1,1,1,1))
            self.waterTopEffect = Sequence(topE1, topE2)
            self.waterTopEffect.loop()
            bottomE1 = LerpColorScaleInterval(waterBottom, 1.5, (.9,.9,.9,1))
            bottomE2 = LerpColorScaleInterval(waterBottom, 1.5, (1,1,1,1))
            self.waterBotEffect = Sequence(bottomE1, bottomE2)
            self.waterBotEffect.loop()
            ShakeFactor = .5
            waterE1 = water.hprInterval(3, (0,0,ShakeFactor), startHpr=(0,0,-ShakeFactor))
            waterE2 = water.hprInterval(3, (0,0,-ShakeFactor), startHpr=(0,0,ShakeFactor))
            self.waterShake = Sequence(waterE1, Wait(.4),  waterE2, Wait(.4))
            self.waterShake.loop()
            
    def __stopWaterEffect(self):
        self.waterTopEffect.finish()
        self.waterBotEffect.finish()
        self.waterShake.finish()
        del self.waterTopEffect, self.waterBotEffect, self.waterShake

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
