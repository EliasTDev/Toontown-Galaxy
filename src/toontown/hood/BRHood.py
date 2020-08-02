from panda3d.core import Fog
from toontown.safezone.BRSafeZoneLoader import BRSafeZoneLoader
from toontown.town.BRTownLoader import BRTownLoader
from toontown.toonbase import ToontownGlobals
from toontown.hood.ToonHood import ToonHood

class BRHood(ToonHood):
    notify = directNotify.newCategory('BRHood')

    ID = ToontownGlobals.TheBrrrgh
    TOWNLOADER_CLASS = BRTownLoader
    SAFEZONELOADER_CLASS = BRSafeZoneLoader
    STORAGE_DNA = 'phase_8/dna/storage_BR.dna'
    SKY_FILE = 'phase_3.5/models/props/BR_sky'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (0.3, 0.6, 1.0, 1.0)

    HOLIDAY_DNA = {
      ToontownGlobals.CHRISTMAS: ['phase_8/dna/winter_storage_BR.dna'],
      ToontownGlobals.HALLOWEEN: ['phase_8/dna/halloween_props_storage_BR.dna']}

    def load(self):
        ToonHood.load(self)

        self.fog = Fog('BRFog')

    def setFog(self):
        if base.wantFog:
            self.fog.setColor(0.9, 0.9, 0.9)
            self.fog.setExpDensity(0.012)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)