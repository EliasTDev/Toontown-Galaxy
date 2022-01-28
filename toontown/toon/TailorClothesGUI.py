from toontown.makeatoon import ClothesGUI
from . import ToonDNA


class TailorClothesGUI(ClothesGUI.ClothesGUI):
    notify = directNotify.newCategory("MakeClothesGUI")

    def __init__(self, doneEvent, swapEvent, tailorId):
        ClothesGUI.ClothesGUI.__init__(self, ClothesGUI.CLOTHES_TAILOR,
                                       doneEvent, swapEvent)
        self.tailorId = tailorId

    def setupScrollInterface(self):
        self.dna = self.toon.getStyle()

        # Handle the case where we're in a shop (clothes aren't randomized,
        # we can't be changing gender, etc.
        if (self.swapEvent is not None):
            self.tops = ToonDNA.getTops(tailorId=self.tailorId)
            self.bottoms = ToonDNA.getBottoms(
                tailorId=self.tailorId)
            # We're off the wheel of choices to start with because we're
            # wearing clothes purchased elsewhere
            self.topChoice = -1
            self.bottomChoice = -1

        # setup the buttons
        self.setupButtons()
