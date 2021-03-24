
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import random

class ToontownLoadingScreen:

    def __init__(self):

        self.__expectedCount = 0
        self.__count = 0

        self.gui = loader.loadModel("phase_3/models/gui/progress-background")

        # Hide the Disney logo in the model itself.
        self.gui.find("**/logo").hide()

        self.banner = loader.loadModel("phase_3/models/gui/toon_council").find("**/scroll")
        self.banner.reparentTo(self.gui)
        self.banner.setScale(0.4,0.4,0.4)
        #load our logo
        self.galaxyLogo = OnscreenImage('phase_3/maps/toontown-logo.png')

        self.galaxyLogo.reparentTo(base.a2dpTopCenter)
        self.galaxyLogo.setScale(self.gui, (0.6, 1.2, 0.4))
        self.galaxyLogo.setTransparency(TransparencyAttrib.MAlpha)
        self.galaxyLogo.setZ(0.61)
        #self.galaxyLogo.setPos(0, 0, -galaxyLogoScale)
        self.galaxyLogo.reparentTo(hidden)

        self.tip = DirectLabel(
            guiId = "ToontownLoadingScreenTip",
            parent = self.banner,
            relief = None,
            text = "",
            text_scale = TTLocalizer.TLStip,
            textMayChange = 1,
            pos = (-1.2,0.0,0.1),
            text_fg = (0.4,0.3,0.2,1),
            text_wordwrap = 13,
            text_align = TextNode.ALeft,
            )

        self.title = DirectLabel(
            guiId = "ToontownLoadingScreenTitle",
            parent = self.gui,
            relief = None,
            pos = (-1.06, 0, -0.77),
            text = "",
            textMayChange = 1,
            text_scale = 0.08,
            text_fg = (0,0,0.5,1),
            text_align = TextNode.ALeft,
            )

        # Hide the running man until we animate him
        self.waitBar = DirectWaitBar(
            guiId = "ToontownLoadingScreenWaitBar",
            parent = self.gui,
            frameSize = (-1.06,1.06,-0.03,0.03),
            pos = (0,0,-0.85),
            text = '',
            )

    def destroy(self):
        self.tip.destroy()
        self.title.destroy()
        self.waitBar.destroy()
        self.banner.removeNode()
        self.galaxyLogo.destroy()
        self.gui.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + "\n" + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory):
        # make the loader bar and draw it.
        self.waitBar['range'] = range
        self.title['text'] = label
        self.tip['text'] = self.getTip(tipCategory)

        self.__count = 0
        self.__expectedCount = range

        if gui:
            # Put the progress gui in front of all the fade action
            self.waitBar.reparentTo(self.gui)
            self.title.reparentTo(self.gui)
            self.gui.reparentTo(aspect2dp, DGG.NO_FADE_SORT_INDEX)
            self.galaxyLogo.reparentTo(self.gui)
            base.setBackgroundColor((0, 0, 46/255, 0))

        else:
            self.waitBar.reparentTo(aspect2dp, DGG.NO_FADE_SORT_INDEX)
            self.title.reparentTo(aspect2dp, DGG.NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
            self.galaxyLogo.reparentTo(hidden)
            base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

        self.waitBar.update(self.__count)

    def end(self):
        # animate end of bar, if needed, then get rid of it
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.galaxyLogo.reparentTo(hidden)
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

    def tick(self):
        self.__count = self.__count + 1
        # update progress bar
        self.waitBar.update(self.__count)
