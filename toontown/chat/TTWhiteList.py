import os
from pandac.PandaModules import *
from direct.showbase import AppRunnerGlobal
from otp.chat.WhiteList import WhiteList
from toontown.toonbase import TTLocalizer
from otp.chat import WhiteListData


class TTWhiteList(WhiteList):
    def __init__(self):

        WhiteList.__init__(self, WhiteListData.WHITELIST)
        self.defaultWord = TTLocalizer.ChatGarblerDefault[0]
