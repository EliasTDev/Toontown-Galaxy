from direct.gui.DirectGui import *
from pandac.PandaModules import *
from . import NPCToons
from . import ToonHead
from . import ToonDNA
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals

class NPCFriendPanel(DirectFrame):

    SOS_PER_PAGE = 8
    def __init__(self, parent = aspect2d, fCallable = 0, **kw):
        self.fCallable = fCallable
        # Define options
        optiondefs = (
            ('relief',        None,                   None),
            ('doneEvent',     None,                   None),
            )
        # Merge keyword options with default options
        self.defineoptions(kw, optiondefs)
        # Initialize superclass
        DirectFrame.__init__(self, parent = parent)
        self.cardList = []
        xOffset = -5.25
        yOffset = 2.3
        count = 0
        self.pos = 0
        for card in self.cardList:
                card.destroy()
        self.cardList = []
        for i in range(8):
            card = NPCFriendCard(parent = self, doneEvent = self['doneEvent'])
            self.cardList.append(card)
            card.setScale(0.8)
            card.setPos(xOffset, 1, yOffset)
            xOffset += 3.5
            count += 1
            if count == 4:
                xOffset = -5.25
                yOffset = -2.3
        # Initialize instance
        self.initialiseoptions(NPCFriendPanel)
        #check if scroll wheel is used (or trackpad scrolling)
        self.accept('wheel_up', self.scrollDown)
        self.accept('wheel_down', self.scrollUp)
        arrow = loader.loadModel('phase_3/models/gui/scroll_arrows_gui.bam')
        arrowImage = (arrow.find('**/FndsLst_ScrollUp'),
                      arrow.find('**/FndsLst_ScrollDN'),
                      arrow.find('**/FndsLst_ScrollUp_Rllvr'))
        self.arrowUp = DirectButton(parent=self, relief = None,
                                    image = arrowImage,
                                    pos = (0, 0, 5),
                                    command = self.scrollDown,
                                    scale = 2,
                                    image_scale = 3,
                                    suppressMouse=False

                                    )
        self.arrowDown = DirectButton(parent=self, relief = None,
                                    image = arrowImage,
                                    pos = (0, 0, -5),
                                    scale = -2,
                                    command = self.scrollUp,
                                    image_scale = 3,
                                    suppressMouse=False
                                    )
        arrow.removeNode()
        self.arrowUp.hide()

    def update(self, friendDict):
        fCallable = self.fCallable
        friendList = list(friendDict.keys())
        cardNumber = 0
        for i in range(self.pos, self.pos + self.SOS_PER_PAGE):
            card = self.cardList[cardNumber]
            if len(friendList) <= i:
                card.update(None, 0, fCallable)
                self.arrowDown.hide()
            else:
                NPCID = friendList[i]
                card.update(NPCID, friendDict[NPCID], fCallable)
                self.arrowDown.show()
            cardNumber += 1

    def destroy(self):
        self.ignore('scrollUp')
        self.ignore('scrollDown')
        DirectFrame.destroy(self)

    def addToIndex(self, index):
        self.pos += (self.SOS_PER_PAGE * index)
        self.posTask()
    
    def subtractToIndex(self, index):
        self.pos -= (self.SOS_PER_PAGE * index)
        self.posTask()



    def posTask(self):
        if self.pos <= 0:
            self.arrowUp.hide()
        else:
            self.arrowUp.show()
        self.update(base.localAvatar.NPCFriendsDict)

    def scrollUp(self):
        #check if down arrow is hidden if its not addtoindex
        if not self.arrowDown.isHidden():
            self.addToIndex(1)
        
    def scrollDown(self):
        #check if up arrow is hidden if its not subtracttoindex
        if not self.arrowUp.isHidden():
            self.subtractToIndex(1)
    

class NPCFriendCard(DirectFrame):
    normalTextColor = (0.3,0.25,0.2,1)
    maxRarity = 5
    sosTracks = (ToontownBattleGlobals.Tracks +
                 ToontownBattleGlobals.NPCTracks)
    def __init__(self, parent = aspect2dp, **kw):
        # Define options
        optiondefs = (
            ('NPCID',     'Uninitialized',        None),
            ('relief',               None,        None),
            ('doneEvent',            None,        None),
            )
        # Merge keyword options with default options
        self.defineoptions(kw, optiondefs)
        # Initialize superclass
        DirectFrame.__init__(self, parent = parent)
        # Initialize instance
        self.initialiseoptions(NPCFriendCard)

        # Front side of the card
        cardModel = loader.loadModel('phase_3.5/models/gui/playingCard')
        self.front = DirectFrame(
            parent = self, relief = None,
            image = cardModel.find('**/card_front'),
            )
        self.front.hide()

        # Back side of the card
        self.back = DirectFrame(
            parent = self, relief = None,
            image = cardModel.find('**/card_back'),
            geom = cardModel.find('**/logo')
            )

        # Detail information about the quest
        self.sosTypeInfo = DirectLabel(
            parent = self.front,
            relief = None,
            text = '',
            text_font = ToontownGlobals.getMinnieFont(),
            text_fg = self.normalTextColor,
            text_scale = 0.35,
            text_align = TextNode.ACenter,
            text_wordwrap = 7.0,
            pos = (0,0,1.6),
            )

        # Toon head
        self.NPCHead = None

        # NPC Name
        self.NPCName = DirectLabel(
            parent = self.front,
            relief = None,
            text = '',
            text_fg = self.normalTextColor,
            text_scale = 0.34,
            text_align = TextNode.ACenter,
            text_wordwrap = 8.0,
            pos = (0, 0, -0.58)
            )

        # Call button (only show during battle
        buttonModels = loader.loadModel(
            "phase_3.5/models/gui/inventory_gui")
        upButton = buttonModels.find("**/InventoryButtonUp")
        downButton = buttonModels.find("**/InventoryButtonDown")
        rolloverButton = buttonModels.find("**/InventoryButtonRollover")
        self.sosCallButton = DirectButton(
            parent = self.front,
            relief = None,
            text = TTLocalizer.NPCCallButtonLabel,
            text_fg = self.normalTextColor,
            text_scale = 0.28,
            text_align = TextNode.ACenter,
            image = (upButton,
                     downButton,
                     rolloverButton,
                     upButton,
                     ),
            image_color = (1.0, 0.2, 0.2, 1),
            # Make the rollover button pop out
            image0_color = Vec4(1.0, 0.4, 0.4, 1),
            # Make the disabled button fade out
            image3_color = Vec4(1.0, 0.4, 0.4, 0.4),
            image_scale = (4.4,1,3.6),
            image_pos = Vec3(0,0,0.08),
            pos = (-0.96, 0, -1.6),
            scale = 1.25,
            command = self.__chooseNPCFriend,
            )
        self.sosCallButton.hide()

        # Info on how many more times one can use this card
        self.sosCountInfo = DirectLabel(
            parent = self.front,
            relief = None,
            text = '',
            text_fg = self.normalTextColor,
            text_scale = 0.4,
            text_align = TextNode.ALeft,
            textMayChange = 1,
            pos = (0.0, 0, -0.9)
            )

        star = loader.loadModel('phase_3.5/models/gui/name_star')
        self.rarityStars = []
        for i in range(self.maxRarity):
            label = DirectLabel(
                parent = self.front,
                relief = None,
                image = star,
                image_scale = 0.2,
                image_color = Vec4(0.502, 0.251, 0.251, 1.000),
                pos = (1.1 - i * 0.24, 0, -1.1)
                )
            label.hide()
            self.rarityStars.append(label)

    def __chooseNPCFriend(self):
        if self['NPCID'] and self['doneEvent']:
            doneStatus = {}
            doneStatus['mode'] = 'NPCFriend'
            doneStatus['friend'] = self['NPCID']
            messenger.send(self['doneEvent'], [doneStatus])

    def destroy(self):
        if(self.NPCHead):
            self.NPCHead.detachNode()
            self.NPCHead.delete()
        DirectFrame.destroy(self)


    def update(self, NPCID, count=0, fCallable=0):

        # Record ID for next update
        oldNPCID = self['NPCID']
        self['NPCID'] = NPCID

        if NPCID != oldNPCID:
            # Update things that only change when NPC ID changes
            if self.NPCHead:
                # New NPC, get rid of old head if it exists
                self.NPCHead.detachNode()
                self.NPCHead.delete()
                
            if NPCID is None:
                # Show back of card
                self.showBack()
                return

            # Show front of card
            self.front.show()
            self.back.hide()

            # Update labels
            self.NPCName['text'] = TTLocalizer.NPCToonNames[NPCID]
            # Creat new toon head
            self.NPCHead = self.createNPCToonHead(NPCID, dimension = 1.4)
            self.NPCHead.reparentTo(self.front)
            self.NPCHead.setZ(0.3)
            # Get details about toon
            track, level, hp, rarity = NPCToons.getNPCTrackLevelHpRarity(NPCID)
            # Update sos type info
            sosText = self.sosTracks[track]
            if track == ToontownBattleGlobals.NPC_RESTOCK_GAGS:
                # In this case level is the track being restocked
                if level == -1:
                    sosText += " All"
                else:
                    sosText += " " + self.sosTracks[level]
            sosText = TextEncoder.upper(sosText)
            self.sosTypeInfo['text'] = sosText
            # Update Rarity stars
            for i in range(self.maxRarity):
                if i < rarity:
                    self.rarityStars[i].show()
                else:
                    self.rarityStars[i].hide()

        if fCallable:
            self.sosCallButton.show()
            self.sosCountInfo.setPos(-0.4, 0, -1.54)
            self.sosCountInfo['text_scale'] = 0.28
            self.sosCountInfo['text_align'] = TextNode.ALeft
        else:
            self.sosCallButton.hide()
            self.sosCountInfo.setPos(0, 0, -0.9)
            self.sosCountInfo['text_scale'] = 0.4
            self.sosCountInfo['text_align'] = TextNode.ACenter

        if count > 0:
            countText = (TTLocalizer.NPCFriendPanelRemaining % (count))
            self.sosCallButton['state'] = DGG.NORMAL
        else:
            countText = "Unavailable"
            self.sosCallButton['state'] = DGG.DISABLED
    
        self.sosCountInfo['text'] = countText

    def showFront(self):
        self.front.show()
        self.back.hide()

    def showBack(self):
        self.front.hide()
        self.back.show()

    def createNPCToonHead(self, NPCID, dimension = 0.5):
        # Given an NPC id create a toon head suitable for framing
        NPCInfo = NPCToons.NPCToonDict[NPCID]
        dnaList = NPCInfo[2]
        #To not break the entire npc list
        eyelashes = NPCInfo[3]
        if eyelashes == 'm':
            eyelashes = 0
        else:
            eyelashes = 1
        if dnaList == 'r':
            dnaList = NPCToons.getRandomDNA(NPCID, eyelashes)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties(*dnaList)
        head = ToonHead.ToonHead()
        head.setupHead(dna, forGui = 1)
        # Insert xform with gets head to uniform size
        self.fitGeometry(head, fFlip = 1, dimension = dimension)
        return head

    def fitGeometry(self, geom, fFlip = 0, dimension = 0.5):
        # Insert an xform which centers geometry on origin and scales it
        # to +/-0.8 in size
        p1 = Point3()
        p2 = Point3()
        geom.calcTightBounds(p1, p2)
        if fFlip:
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = dimension/biggest
        # find midpoint
        mid = (p1 + d/2.0) * s
        geomXform = hidden.attachNewNode('geomXform')
        for child in geom.getChildren():
            child.reparentTo(geomXform)
        geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2],
                                 180, 0, 0,
                                 s, s, s)
        geomXform.reparentTo(geom)
    


        

