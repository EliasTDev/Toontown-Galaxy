"""Panda mockery - run pieces of code without running the entire server."""
# prepare the python environment
import builtins
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./dependencies/panda'))

# Patch the widgets to print the coords on LMB
from direct.gui.DirectGui import DGG
from direct.gui.DirectGuiBase import DirectGuiWidget
old_init = DirectGuiWidget.__init__


def new_init(self, *a, **kw):
    old_init(self, *a, **kw)
    self.bind(DGG.B1PRESS, lambda x: print(self.getPos()))


DirectGuiWidget.__init__ = new_init

# prepare the toontown environment
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader
from panda3d.core import WindowProperties, getModelPath, Filename, loadPrcFile

getModelPath().appendDirectory(Filename.expandFrom(os.path.abspath('./resources')))  # type: ignore
loadPrcFile('etc/Configrc.prc')

builtins.directNotify = directNotify


class FakeLocalToon:
    money = 100
    bankMoney = 5432
    maxCarry = 120


class MockeryBase(ShowBase):
    def __init__(self):
        super().__init__()
        builtins.base = self
        builtins.loader = Loader(self)

        properties = WindowProperties()
        properties.setSize(1280, 720)
        properties.setTitle('Toontown Mockery by Wizzerinus')
        self.win.requestProperties(properties)

        self.localAvatar = FakeLocalToon()
        self.autolock = False


base = MockeryBase()

# load the mockery file of your choice
from .InventoryUI import InventoryUI

base.invUI = InventoryUI()
base.run()
