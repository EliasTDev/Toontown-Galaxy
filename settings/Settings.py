import json, os

from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *

class Settings(object):
    notify = DirectNotifyGlobal.directNotify.newCategory('Settings')


    def __init__(self, fileName='user/settings.json'):
        #Name of the file
        self.fileName = fileName
        #Make the directory if it doesnt exist for the file to be in
        if os.path.dirname(self.fileName) and not os.path.exists(os.path.dirname(self.fileName)):
            os.makedirs(os.path.dirname(self.fileName))
        #Attempt to load the settings file
        try:
            with open(self.fileName, 'r') as f:
                self.settings = json.load(f)
        except:
            #Define empty settings dict
            self.settings = {}

    def getOption(self, category, attribute, default):
        return self.settings.get(category, {}).get(attribute, default)

    def getFloat(self, category, attribute, default=1):
        value = self.getOption(category, attribute, default)
        if isinstance(value, float):
            return value
        else:
            return default

    def getBool(self, category, attribute, default=False):
        value = self.getOption(category, attribute, default)
        if isinstance(value, bool):
            return value
        else:
            return default

    def getInt(self, category, attribute, default=0):
        value = self.getOption(category, attribute, default)
        if isinstance(value, (int)):
            return int(value)
        else:
            return default


    def getList(self, category, attribute, default=[], expectedLength =2):
        value = self.getOption(category, attribute, default)
        if isinstance(value, list) and len(value) == expectedLength:
            return value
        else:
            return default
    def doSavedSettingsExist(self):
        return os.path.exists(self.fileName)

    def writeSettings(self):
        with open(self.fileName, "w+") as f:
            json.dump(self.settings, f, indent=4)

    def updateSetting(self, category, attribute, value):
        if not self.settings.get(category):
            self.settings[category] = {}
        self.settings[category][attribute] = value
        self.writeSettings()
        
    def loadFromSettings(self):
        # Setting for toggling stretched screen.
        # Stretched screen forces the aspect ratio to be 4:3, or 1.333.
        stretchedScreen = self.getBool('game', 'stretched-screen', False)
        if stretchedScreen:
            loadPrcFileData('toonBase Settings Stretched Screen', 'aspect-ratio 1.333')
        else:
            self.updateSetting('game', 'stretched-screen', stretchedScreen)
