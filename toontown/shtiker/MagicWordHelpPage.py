from toontown.spellbook.MagicWordIndex import *
from toontown.toon import ToonDNA
from toontown.toon import Toon
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.gui.DirectGui import *
from direct.showbase import PythonUtil
from panda3d.core import *
from toontown.shtiker.ShtikerPage import ShtikerPage


class MagicWordsHelpTabPage(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'MagicWordsHelpTabPage')

    def __init__(self, parent=aspect2d):
        self.currentSizeIndex = None
        self._parent = parent
        DirectFrame.__init__(
            self, parent=self._parent, relief=None, pos=(
                0.0, 0.0, 0.0), scale=(
                1.0, 1.0, 1.0))

        self.load()

    def load(self):
        self.magicWords = []
        self.setupMagicWords()

        friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        PATButton = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
        quitButton = loader.loadModel('phase_3/models/gui/quit_button')
        cdrGui = loader.loadModel(
            'phase_3.5/models/gui/tt_m_gui_sbk_codeRedemptionGui')
        avatarPanelGui = loader.loadModel(
            'phase_3.5/models/gui/avatar_panel_gui')
        self.helpLabel = DirectLabel(
            parent=self,
            text="""This page contains a list of all of the Magic Words
                                             that can be used in-game.""",
            text_scale=0.06,
            text_wordwrap=12,
            text_align=TextNode.ALeft,
            textMayChange=1,
            pos=(
                0.058,
                0,
                0.403),
            relief=None)
        self.searchLabel = DirectLabel(parent=self, text='Search',
                                       text_scale=0.06, text_wordwrap=12,
                                       text_align=TextNode.ACenter, textMayChange=1,
                                       pos=(0.439, 0, -0.2), relief=None,)
        self.searchFrame = DirectFrame(parent=self, image=cdrGui.find(
            '**/tt_t_gui_sbk_cdrCodeBox'), pos=(0.439, 0.0, -0.3225), scale=0.7, relief=None,)
        self.searchEntry = DirectEntry(
            parent=self,
            text_scale=0.06,
            width=7.75,
            textMayChange=1,
            pos=(
                0.209,
                0,
                -0.3325),
            text_align=TextNode.ALeft,
            backgroundFocus=0,
            focusInCommand=self.toggleEntryFocusCommand,
            relief=None)
        self.searchEntry.bind(DGG.TYPE, self.updateMagicWordSearch)
        self.searchEntry.bind(DGG.ERASE, self.updateMagicWordSearch)
        self.activatorLabel = DirectLabel(
            parent=self,
            text='Activator: ' + "N/A",
            text_scale=0.06,
            text_wordwrap=12,
            text_align=TextNode.ALeft,
            textMayChange=1,
            pos=(
                0.058,
                0,
                0.15),
            relief=None)
        self.totalMagicWordsLabel = DirectLabel(parent=self,
                                                text="Total Magic Words: " + str(len(self.magicWords)),
                                                text_scale=0.06, text_wordwrap=12,
                                                text_align=TextNode.ALeft, textMayChange=1,
                                                pos=(0.058, 0, 0.05), relief=None)
        self.currentLabel = DirectLabel(parent=self,
                                        text='Current: ' + 'N/A',
                                        text_scale=0.06, text_wordwrap=12,
                                        text_align=TextNode.ALeft, textMayChange=1,
                                        pos=(0.058, 0, -0.05), relief=None)
        self.copyToChatButton = DirectButton(
            parent=self,
            image=(
                quitButton.find('**/QuitBtn_UP'),
                quitButton.find('**/QuitBtn_DN'),
                quitButton.find('**/QuitBtn_RLVR')),
            image_scale=(
                0.7,
                1,
                1),
            text="Copy To Chat",
            text_scale=0.04,
            text_pos=(
                0,
                -0.01),
            pos=(
                0.629,
                0.0,
                -0.5325),
            relief=None,
            command=self.copyToChatCommand)
        self.moreInfoButton = DirectButton(
            parent=self,
            image=(
                quitButton.find('**/QuitBtn_UP'),
                quitButton.find('**/QuitBtn_DN'),
                quitButton.find('**/QuitBtn_RLVR')),
            image_scale=(
                0.7,
                1,
                1),
            text="More Info",
            text_scale=0.04,
            text_pos=(
                0,
                -0.01),
            pos=(
                0.249,
                0.0,
                -0.5325),
            relief=None,
            command=self.showMoreInfoPanelCommand)
        self.scrollList = DirectScrolledList(parent=self, forceHeight=0.07,
                                             pos=(-0.5, 0, 0),
                                             incButton_image=(friendsGui.find('**/FndsLst_ScrollUp'),
                                                              friendsGui.find('**/FndsLst_ScrollDN'),
                                                              friendsGui.find('**/FndsLst_ScrollUp_Rllvr'),
                                                              friendsGui.find('**/FndsLst_ScrollUp')),
                                             incButton_relief=None, incButton_scale=(1.3, 1.3, -1.3),
                                             incButton_pos=(0.08, 0, -0.60), incButton_image3_color=Vec4(1, 1, 1, 0.2),
                                             decButton_image=(friendsGui.find('**/FndsLst_ScrollUp'),
                                                              friendsGui.find('**/FndsLst_ScrollDN'),
                                                              friendsGui.find('**/FndsLst_ScrollUp_Rllvr'),
                                                              friendsGui.find('**/FndsLst_ScrollUp')),
                                             decButton_relief=None, decButton_scale=(1.3, 1.3, 1.3),
                                             decButton_pos=(0.08, 0, 0.52), decButton_image3_color=Vec4(1, 1, 1, 0.2),
                                             itemFrame_pos=(-0.237, 0, 0.41), itemFrame_scale=1.0,
                                             itemFrame_relief=DGG.SUNKEN,
                                             itemFrame_frameSize=(-0.05, 0.66, -0.98, 0.07),
                                             itemFrame_frameColor=(0.85, 0.95, 1, 1),
                                             itemFrame_borderWidth=(0.01, 0.01),
                                             numItemsVisible=14, items=self.magicWords)
        self.slider = DirectSlider(parent=self, range=(len(self.magicWords), 0),
                                   scale=(0.7, 0.7, 0.515), pos=(-0.1, 0, -0.045),
                                   pageSize=1, orientation=DGG.VERTICAL,
                                   command=self.scrollListToCommand,
                                   thumb_geom=(PATButton.find('**/QuitBtn_UP'),
                                               PATButton.find('**/QuitBtn_DN'),
                                               PATButton.find('**/QuitBtn_RLVR'),
                                               PATButton.find('**/QuitBtn_UP')),
                                   thumb_relief=None, thumb_geom_hpr=(0, 0, -90),
                                   thumb_geom_scale=(0.5, 1, 0.5))
        self.magicWordInfoFrame = DirectFrame(
            parent=self, relief=None, pos=(
                0.0, 0.0, -0.05), scale=0.9, geom=DGG.getDefaultDialogGeom(), geom_scale=(
                1.4, 1, 1), geom_color=ToontownGlobals.GlobalDialogColor)
        self.magicWordTitleLabel = DirectLabel(
            parent=self.magicWordInfoFrame,
            relief=None,
            text='N/A',
            text_scale=0.12,
            textMayChange=1,
            pos=(
                0,
                0,
                0.3500))
        self.magicWordInfoLabel = DirectLabel(
            parent=self.magicWordInfoFrame,
            relief=None,
            text='N/A',
            text_scale=0.06,
            text_wordwrap=20,
            text_align=TextNode.ALeft,
            textMayChange=1,
            pos=(
                -0.6,
                0,
                0.2))
        self.magicWordCloseButton = DirectButton(
            parent=self.magicWordInfoFrame,
            image=(
                avatarPanelGui.find('**/CloseBtn_UP'),
                avatarPanelGui.find('**/CloseBtn_DN'),
                avatarPanelGui.find('**/CloseBtn_Rllvr'),
                avatarPanelGui.find('**/CloseBtn_UP')),
            relief=None,
            scale=1.5,
            pos=(
                0.6,
                0,
                -0.4),
            command=self.hideInfoPanelCommand)
        self.magicWordInfoFrame.hide()
        friendsGui.removeNode()
        PATButton.removeNode()
        quitButton.removeNode()
        cdrGui.removeNode()
        avatarPanelGui.removeNode()

    def unload(self):
        for magicWord in self.magicWords:
            magicWord.destroy()
            del magicWord

        guiList = [
            self.helpLabel,
            self.searchLabel,
            self.searchFrame,
            self.searchEntry,
            self.activatorLabel,
            self.totalMagicWordsLabel,
            self.currentLabel,
            self.copyToChatButton,
            self.moreInfoButton,
            self.scrollList,
            self.slider,
            self.magicWordTitleLabel,
            self.magicWordInfoLabel,
            self.magicWordCloseButton,
            self.magicWordInfoFrame]

        for gui in guiList:
            gui.destroy()
            del gui

    def exit(self):
        for magicWord in self.magicWords:
            if magicWord['state'] != DGG.NORMAL:
                magicWord['state'] = DGG.NORMAL

        self.activatorLabel['text'] = 'Activator: ' + base.cr.magicWordManager.chatPrefix + \
            ' (' + str(MagicWordConfig.PREFIX_ALLOWED.index(base.cr.magicWordManager.chatPrefix)) + ')'
        self.currentLabel['text'] = 'Current: ' + 'N/A'
        self.ignore('mouse1')
        self.toggleEntryFocusCommand(True)
        self.searchEntry.set('')
        self.updateMagicWordSearch()
        self.hideInfoPanelCommand()
        self.hide()

    def enter(self):
        for word in self.magicWords:
            if word['state'] != DGG.NORMAL:
                word['state'] = DGG.NORMAL

        self.activatorLabel['text'] = 'Activator: ' + base.cr.magicWordManager.chatPrefix + \
            ' (' + str(MagicWordConfig.PREFIX_ALLOWED.index(base.cr.magicWordManager.chatPrefix)) + ')'
        self.currentLabel['text'] = 'Current: ' + 'N/A'
        self.accept('mouse1', self.toggleEntryFocusCommand, extraArgs=[True])
        self.searchEntry.set('')
        self.updateMagicWordSearch()
        self.hideInfoPanelCommand()
        self.show()

    def toggleEntryFocusCommand(self, lose=False):
        if lose:
            self.searchEntry['focus'] = 0
            base.localAvatar.chatMgr.fsm.request('mainMenu')
        else:
            base.localAvatar.chatMgr.fsm.request('otherDialog')

    def scrollListToCommand(self):
        self.scrollList.scrollTo(int(self.slider['value']))

    def showMagicWordInfo(self, magicWordNum):
        for magicWord in self.magicWords:
            if magicWord['state'] != DGG.NORMAL:
                magicWord['state'] = DGG.NORMAL

        magicWordName = self.magicWords[magicWordNum]
        magicWordName['state'] = DGG.DISABLED
        self.currentLabel['text'] = 'Current: ' + magicWordName['text']

    def setupMagicWords(self, returnMagicWords=False):
        magicWords = []

        for magicWordName in magicWordIndex:
            magicWord = magicWordIndex[magicWordName]
            if magicWord['classname'] not in magicWords:
                magicWords.append(magicWord['classname'])

        sortedMagicWords = sorted(magicWords)

        numMagicWords = len(sortedMagicWords)
        if returnMagicWords:
            return numMagicWords

        currentMagicWordIndex = 0
        while currentMagicWordIndex < numMagicWords:
            newMagicWordButton = DirectButton(
                parent=self,
                relief=None,
                text=sortedMagicWords[currentMagicWordIndex],
                text_align=TextNode.ALeft,
                text_scale=0.05,
                text1_bg=Vec4(
                    0.5,
                    0.9,
                    1,
                    1),
                text2_bg=Vec4(
                    1,
                    1,
                    0,
                    1),
                text3_fg=Vec4(
                    0.4,
                    0.8,
                    0.4,
                    1),
                textMayChange=0,
                command=self.showMagicWordInfo,
                extraArgs=[currentMagicWordIndex])
            self.magicWords.append(newMagicWordButton)
            currentMagicWordIndex += 1

    def copyToChatCommand(self):
        magicWordName = None
        for magicWord in self.magicWords:
            if magicWord['state'] != DGG.NORMAL:
                magicWordName = magicWord['text']
                break

        if not magicWordName:
            return

        phrase = base.cr.magicWordManager.chatPrefix + magicWordName + ' '
        localAvatar.book.closeBook()
        localAvatar.chatMgr.fsm.request('mainMenu')
        localAvatar.chatMgr.chatInputNormal.typeCallback(None)
        localAvatar.chatMgr.chatInputNormal.chatEntry.enterText(phrase)

    def updateMagicWordSearch(self, extraArgs=None):
        searchTerm = self.searchEntry.get().lower()

        magicWordCount = len(self.magicWords)
        if magicWordCount == 0:
            magicWordCount = 1

        self.totalMagicWordsLabel['text'] = 'Total Magic Words:' + \
            str(len(self.magicWords))
        self.scrollList['items'] = self.magicWords
        self.slider['range'] = (magicWordCount, 0)

    def hideInfoPanelCommand(self):
        self.magicWordTitleLabel['text'] = 'N/A'
        self.magicWordInfoLabel['text'] = 'N/A'

        self.magicWordInfoFrame.hide()

    def showMoreInfoPanelCommand(self):
        magicWordName = None
        for magicWord in self.magicWords:
            if magicWord['state'] != DGG.NORMAL:
                magicWordName = magicWord['text']
                break

        if not magicWordName:
            return

        magicWordInfo = magicWordIndex[magicWordName.lower()]
        magicWordText = 'Description: ' + magicWordInfo['desc']
        prefix = base.cr.magicWordManager.chatPrefix
        if not magicWordInfo['example']:
            exampleText = 'Example: ' + prefix + magicWordName.lower()
        else:
            exampleText = 'Example: ' + prefix + magicWordName.lower() + ' ' + \
                magicWordInfo['example']
        aliasText = 'Aliases: '
        for alias in magicWordInfo['aliases']:
            aliasText += alias
            if magicWordInfo['aliases'].index(
                    alias) != len(magicWordInfo['aliases']) - 1:
                aliasText += ', '
        accessLevelText = 'Access Level: ' + magicWordInfo['access'] + ' (' + str(
            OTPGlobals.AccessLevelName2Int.get(magicWordInfo['access'])) + ')'

        lineBreak = '\n\n'
        infoText = magicWordText + lineBreak + exampleText + \
            lineBreak + aliasText + lineBreak + accessLevelText

        self.magicWordTitleLabel['text'] = magicWordName
        self.magicWordInfoLabel['text'] = infoText

        self.magicWordInfoFrame.show()


PageMode = PythonUtil.Enum('Words')


class MagicWordsHelpPage(ShtikerPage):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordsHelpPage')

    def __init__(self):
        ShtikerPage.__init__(self)

    def load(self):
        ShtikerPage.load(self)
        self.magicWordsHelpTabPage = MagicWordsHelpTabPage(self)
        self.magicWordsHelpTabPage.hide()
        self.title = DirectLabel(
            parent=self,
            text='Magic Words Help Page',
            relief=None,
            text_scale=0.12,
            pos=(
                0,
                0,
                0.61))

    def enter(self):
        self.setMode(PageMode.Words, updateAnyways=1)
        ShtikerPage.enter(self)

    def exit(self):
        self.magicWordsHelpTabPage.exit()
        ShtikerPage.exit(self)

    def unload(self):
        self.magicWordsHelpTabPage.unload()
        del self.title
        ShtikerPage.unload(self)

    def setMode(self, mode, updateAnyways=0):
        messenger.send('wakeup')
        if not updateAnyways:
            if self.mode == mode:
                return
            else:
                self.mode = mode
        if mode == PageMode.Words:
            self.mode = PageMode.Words
            self.title['text'] = 'Magic Words Help Page'
            self.magicWordsHelpTabPage.enter()
        else:
            raise(Exception, f'WordPage::setMode - Invalid Mode {mode}')
