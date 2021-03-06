from direct.showbase.PythonUtil import Functor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.makeatoon import ClothesGUI
from . import ClosetGlobals
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class ClosetGUI(ClothesGUI.ClothesGUI):
    # Closet class: contains methods for cycling through and
    # selecting clothes from a toons closet
    # (not necessarily one's own closet)
    notify = directNotify.newCategory("ClosetGUI")

    def __init__(self, isOwner,
                 doneEvent, cancelEvent, swapEvent, deleteEvent,
                 topList = None, botList = None):
        ClothesGUI.ClothesGUI.__init__(self, ClothesGUI.CLOTHES_CLOSET,
                                       doneEvent, swapEvent)
        self.toon = None
        self.topsList = topList
        self.bottomsList = botList
        self.isOwner = isOwner
        self.deleteEvent = deleteEvent
        self.cancelEvent = cancelEvent
        self.verify = None

    def load(self):
        ClothesGUI.ClothesGUI.load(self)
        self.gui = loader.loadModel("phase_3/models/gui/create_a_toon_gui")
        self.cancelButton = DirectButton(
            relief = None,
            image = (self.gui.find("**/CrtAtoon_Btn2_UP"),
                     self.gui.find("**/CrtAtoon_Btn2_DOWN"),
                     self.gui.find("**/CrtAtoon_Btn2_RLLVR"),
                     ),
            pos = (0.15, 0, -0.85),
            command = self.__handleCancel,
            text = ("", TTLocalizer.MakeAToonCancel,
                    TTLocalizer.MakeAToonCancel),
            text_font = ToontownGlobals.getInterfaceFont(),
            text_scale = 0.08,
            text_pos = (0,-0.03),
            text_fg = (1,1,1,1),
            text_shadow = (0,0,0,1),
            )
        self.cancelButton.hide()

        # special buttons for owner of closet (edit buttons)
        if (self.isOwner):
            trashcanGui = loader.loadModel("phase_3/models/gui/trashcan_gui.bam")
            trashImage = (trashcanGui.find("**/TrashCan_CLSD"),
                          trashcanGui.find("**/TrashCan_OPEN"),
                          trashcanGui.find("**/TrashCan_RLVR"))
            self.trashPanel = DirectFrame(
                parent = aspect2d,
                image = DGG.getDefaultDialogGeom(),
                image_color = (1, 1, 0.75, .8),
                image_scale = (0.36, 0, 0.75),
                pos = (-.86, 0, -.05),
                relief=None
                )

            self.topTrashButton = DirectButton(
                parent = self.trashPanel,
                image = trashImage,
                relief = None,
                #pos = (0.67, 0, 0.04),
                pos = (-0.09, 0, 0.2),
                command = self.__handleDelete,
                extraArgs = [ClosetGlobals.SHIRT],
                scale = (.5,.5,.5),
                text = TTLocalizer.ClosetDeleteShirt,
                text_font = ToontownGlobals.getInterfaceFont(),
                text_scale = 0.12,
                text_pos = (0.3,0),
                text_fg = (.8,.2,.2,1),
                text_shadow = (0,0,0,1),
                textMayChange = 0,
                )
            
            self.bottomTrashButton = DirectButton(
                parent = self.trashPanel,
                image = trashImage,
                relief = None,
                textMayChange = 1,
                #pos = (0.67, 0, -0.36),
                pos = (-0.09, 0, -0.2),
                command = self.__handleDelete,
                extraArgs = [ClosetGlobals.SHORTS],
                scale = (.5,.5,.5),
                text = TTLocalizer.ClosetDeleteShorts,
                text_font = ToontownGlobals.getInterfaceFont(),
                text_scale = 0.12,
                text_pos = (0.3,0),
                text_fg = (.8,.2,.2,1),
                text_shadow = (0,0,0,1),
                )
            
            self.button = DirectButton(
                relief = None,
                image = (self.gui.find("**/CrtAtoon_Btn1_UP"),
                         self.gui.find("**/CrtAtoon_Btn1_DOWN"),
                         self.gui.find("**/CrtAtoon_Btn1_RLLVR"),
                         ),
                pos = (-0.15, 0, -0.85),
                command = self.__handleButton,
                text = ("", TTLocalizer.MakeAToonDone,
                        TTLocalizer.MakeAToonDone),
                text_font = ToontownGlobals.getInterfaceFont(),
                text_scale = 0.08,
                text_pos = (0,-0.03),
                text_fg = (1,1,1,1),
                text_shadow = (0,0,0,1),
                )
            trashcanGui.removeNode()            

    def unload(self):
        self.ignore("verifyDone")
        ClothesGUI.ClothesGUI.unload(self)
        self.cancelButton.destroy()
        del self.cancelButton

        if self.isOwner:
            self.topTrashButton.destroy()
            self.bottomTrashButton.destroy()
            self.button.destroy()
            del self.topTrashButton
            del self.bottomTrashButton
            del self.button
            self.trashPanel.destroy()
            del self.trashPanel

        if self.verify:
            self.verify.cleanup()
            del self.verify

    def showButtons(self):
        ClothesGUI.ClothesGUI.showButtons(self)
        self.cancelButton.show()
        if self.isOwner:
            self.topTrashButton.show()
            self.bottomTrashButton.show()
            self.button.show()
            
    def hideButtons(self):
        ClothesGUI.ClothesGUI.hideButtons(self)
        self.cancelButton.hide()
        if self.isOwner:
            self.topTrashButton.hide()
            self.bottomTrashButton.hide()
            self.button.hide()
    
    def setupScrollInterface(self):
        self.notify.debug("setupScrollInterface")
    
        self.dna = self.toon.getStyle()
        #self.gender = self.dna.getGender()
        self.swappedTorso = 0

        # if we already have a topsList, it means we are looking at another
        # toons closet, and the server has given us the list of tops and bottoms
        if self.topsList == None:
            self.topsList = self.toon.getClothesTopsList()
        if self.bottomsList == None:
            self.bottomsList = self.toon.getClothesBottomsList() 

        # set up the clothes lists for the scrollInterface
        self.tops = []  
        self.bottoms = []
        # stick our current clothes in the list
        self.tops.append((self.dna.topTex, self.dna.topTexColor, self.dna.sleeveTex, self.dna.sleeveTexColor))
        self.bottoms.append((self.dna.botTex, self.dna.botTexColor))
        # stick tops and bottoms into the correct format
        i = 0
        while i < len(self.topsList):
            self.tops.append((self.topsList[i], self.topsList[i+1], self.topsList[i+2], self.topsList[i+3]))
            i = i+4

        i = 0
        while i < len(self.bottomsList):
            self.bottoms.append((self.bottomsList[i], self.bottomsList[i+1]))
            i = i+2
            
        # our current clothes are index=0 in the tops and bottoms lists
        self.topChoice = 0
        self.bottomChoice = 0
        # set texture to start of clothes choices
        self.swapTop(0)
        self.swapBottom(0)
        if self.isOwner:
            self.updateTrashButtons()
            
        self.setupButtons()

    def updateTrashButtons(self):
        if len(self.tops) < 2:
            self.topTrashButton['state'] = DGG.DISABLED
        else:
            self.topTrashButton['state'] = DGG.NORMAL
        if len(self.bottoms) < 2:
            self.bottomTrashButton['state'] = DGG.DISABLED
        else:
            self.bottomTrashButton['state'] = DGG.NORMAL

        # update the delete text for bottoms
        if self.toon:
            if self.toon.style.torso[1] == 'd':
                self.bottomTrashButton['text'] = TTLocalizer.ClosetDeleteSkirt
            else:
                self.bottomTrashButton['text'] = TTLocalizer.ClosetDeleteShorts
            
        

    
    def swapBottom(self, offset):
        # override swap bottom to allow cross dressing
        
        length = len(self.bottoms)
        self.bottomChoice += offset
        if (self.bottomChoice <= 0):
            self.bottomChoice = 0
        # ghost the pickers if at the end of the 'wheel'
        assert(self.notify.debug("bottoms: choice = %s, length = %s" % (self.bottomChoice, length)))
        
        self.updateScrollButtons(self.bottomChoice, length, 0,
                                 self.bottomLButton, self.bottomRButton)
        if ((self.bottomChoice < 0) or (self.bottomChoice >= len(self.bottoms))
            or (len(self.bottoms[self.bottomChoice]) != 2)):
            self.notify.warning("bottomChoice index is out of range!")
            return None
        self.toon.style.botTex = self.bottoms[self.bottomChoice][0]
        self.toon.style.botTexColor = self.bottoms[self.bottomChoice][1]
        assert(self.notify.debug("bottomChoice: %s" % (self.bottomChoice)))
        assert(self.notify.debug("shorts: %d tex, %d texcolor" % (self.toon.style.botTex, self.toon.style.botTexColor)))

        #if (self.genderChange == 1):
          #  if self.bottomChoice > 0:
         #       self.__handleGenderBender(1)
         #   else:
         #       self.__handleGenderBender(0)

        if (self.toon.generateToonClothes() == 1):
            self.toon.loop("neutral", 0)
            self.swappedTorso = 1

        if self.isOwner:
            self.updateTrashButtons()

        if (self.swapEvent != None):
            messenger.send(self.swapEvent)


            
    def removeTop(self, index):
        listLen = len(self.tops) 
        if index < listLen:
            del self.tops[index]
            # adjust the index into the list
            if self.topChoice > index:
                self.topChoice -= 1            
            elif self.topChoice == index:
                self.topChoice = 0
            return 1
        return 0
                
    def removeBottom(self, index):
        listLen = len(self.bottoms) 
        if index < listLen:
            del self.bottoms[index]
            # adjust the index into the list
            if self.bottomChoice > index:
                self.bottomChoice -= 1
            elif self.bottomChoice == index:
                self.bottomChoice = 0
            return 1
        return 0
                
    def __handleButton(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)
        messenger.send('wakeup')
        
    def __handleCancel(self):
        messenger.send(self.cancelEvent)
        messenger.send('wakeup')
        
    def __handleDelete(self, t_or_b):
        # prompt the user to verify purchase
        if t_or_b == ClosetGlobals.SHIRT:
            item = TTLocalizer.ClosetShirt
        else:
            if self.toon.style.torso[1] == 'd':
                item = TTLocalizer.ClosetSkirt
            else:
                item = TTLocalizer.ClosetShorts
                
        self.verify = TTDialog.TTGlobalDialog(
            doneEvent = "verifyDone",
            message = TTLocalizer.ClosetVerifyDelete % item,
            style = TTDialog.TwoChoice)
        self.verify.show()
        self.accept("verifyDone", Functor(self.__handleVerifyDelete, t_or_b))
        messenger.send('wakeup')
        
    def __handleVerifyDelete(self, t_or_b):
        status = self.verify.doneStatus
        self.ignore("verifyDone")
        self.verify.cleanup()
        del self.verify
        self.verify = None
        if (status == "ok"):
            messenger.send(self.deleteEvent, [t_or_b])
        messenger.send('wakeup')    
