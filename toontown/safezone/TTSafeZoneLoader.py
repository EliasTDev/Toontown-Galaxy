import random

from direct.fsm import ClassicFSM, State
from panda3d.core import *
#from toontown.building import EndlessSuitInterior
from toontown.launcher import DownloadForceAcknowledge

from . import SafeZoneLoader, TTPlayground
from . import Playground


class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(
            self, hood, parentFSM, doneEvent)
      #  self.fsm.addState(State.State('endlessSuitInterior',
       #                               self.enterEndlessSuitInterior,
        #                              self.exitEndlessSuitInterior,
         #                             ['quietZone',
          #                             'playground', # Win bldg
           #                            ]))
       # for stateName in ['quietZone']:
        #    state = self.fsm.getStateNamed(stateName)
        #    state.addTransition('endlessSuitInterior')
       # self.fsm.addState(State.State('playground',
        #                              self.enterPlayground,
         #                             self.exitPlayground,
          #                            ['quietZone',
           #                            'endlessSuitInterior'  # Elevator

            #                           ]))
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = "phase_4/audio/bgm/TC_nbrhood.ogg"
        self.activityMusicFile = "phase_3.5/audio/bgm/TC_SZ_activity.ogg"
        self.dnaFile = "phase_4/dna/toontown_central_sz.dna"
        self.safeZoneStorageDNAFile = "phase_4/dna/storage_TT_sz.dna"

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = list(map(base.loader.loadSfx, [
            'phase_4/audio/sfx/SZ_TC_bird1.ogg',
            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
            'phase_4/audio/sfx/SZ_TC_bird3.ogg']))

    def unload(self):
        del self.birdSound
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)

    def enterPlayground(self, requestStatus):
        super().enterPlayground(requestStatus)

    def exitPlayground(self):
        super().exitPlayground()

   # def enterEndlessSuitInterior(self, requestStatus):
    #    self.placeClass = EndlessSuitInterior.EndlessSuitInterior
     #   self.enterPlace(requestStatus)
      #  self.hood.spawnTitleText('Endless Cog Building')

    #def exitEndlessSuitInterior(self):
     #   self.exitPlace()
      #  self.placeClass = None

    #def getExteriorPlaceClass(self):
     #   return self.playgroundClass
