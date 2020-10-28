#TODO there is a lot of things we need to get done in here to read from a preferences file or settings file
class Settings:
    GL = 0
    DX7 = 1
    DX8 = 5

    @staticmethod
    def readSettings():
        pass  # TODO

    @staticmethod
    def writeSettings():
        pass  # TODO

    @staticmethod
    def setWindowedMode(_):
        pass #TODO

    @staticmethod
    def getWindowedMode():
        return 1

    @staticmethod
    def setMusic(_):
        pass #TODO

    @staticmethod
    def getMusic():
        return 1
    @staticmethod
    def getMusicVolume():
        return 1 #TODO 

    @staticmethod
    def setSfx(_):
        pass #TODO

    @staticmethod
    def getSfxVolume():
        return 1 #TODO

    @staticmethod
    def getSfx():
        return 1

    @staticmethod
    def setToonChatSounds(_):
        pass #TODO

    @staticmethod
    def getToonChatSounds():
        return 1

    @staticmethod
    def setResolutionDimensions(_, __):
        pass #TODO

    @staticmethod
    def getResolution():
        return 1

    @staticmethod
    def setEmbeddedMode(_):
        pass #TODO

    @staticmethod
    def getEmbeddedMode():
        return 0

    @staticmethod
    def doSavedSettingsExist():
        return 0

    @staticmethod
    def setAcceptingNewFriends(_):
        pass #TODO

    @staticmethod
    def getAcceptingNewFriends():
        return 1

    @staticmethod
    def setAcceptingNonFriendWhispers(_):
        pass #TODO

    @staticmethod
    def getAcceptingNonFriendWhispers():
        return 1
