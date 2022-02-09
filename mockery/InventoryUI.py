from toontown.toon.ToonDNA import ToonDNA
from toontown.toon.modular_im.MIMClient import MIMClient
from toontown.town.BattleUIController import BattleUIController


class FakeCogPanel:
    displayName = 'Legal Eagle\nLawbot\nLevel 10'
    currHP = 105
    maxHP = 132

    def getStyleName(self):
        return 'le'


class FakeToonPanel:
    hp = 50
    maxHp = 100

    def isLocal(self):
        return self.local

    def __init__(self, local=False):
        style = bytes.fromhex('741402020000030003050400000000000000000000000012001212')
        self.style = ToonDNA(style)
        self.local = local

    def getName(self):
        return 'Captain Leonardo Crunchensprocket'


class InventoryUI:
    def __init__(self):
        self.mim = MIMClient(base.localAvatar, [
            [0, [0, 0, 0, 0, 0, 0, 4, 3, 2, 1], 10, 6000],
            [1, [0, 0, 0, 0, 0, 0, 4, 3, 2, 1], 10, 5600],
            [2, [0, 0, 0, 0, 0, 0, 4, 3, 2, 0], 9, 5000],
            [3, [0, 0, 0, 0, 0, 5, 3, 1, 0, 0], 8, 4000],
            [4, [0, 0, 0, 0, 5, 3, 1, 0, 0, 0], 7, 3300],
            [5, [5, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, 15],
            [6, [5, 4, 2, 0, 0, 0, 0, 0, 0, 0], 3, 135],
            [7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0],
            [8, [5, 5, 3, 3, 0, 0, 0, 0, 0, 0], 4, 550],
        ])
        base.localAvatar.inventory = self.mim
        self.mim.setActivateMode('battle')

        cog = FakeCogPanel()
        toon = FakeToonPanel()
        localtoon = FakeToonPanel(True)

        self.battleUI = BattleUIController()
        base.battleUI = self.battleUI
        self.battleUI.adjustCogsAndToons([cog, cog, cog], [], [], [toon, localtoon, toon])
        self.battleUI.request('AttackChoice')
