import time 
from ctypes import *
from direct.task import Task 
from pypresence import Presence
clientId  = "796502813353050122"
RPC = Presence(clientId)
RPC.connect()
class DiscordRPC(object):

    zone2imgdesc = {} #TODO add images for each zone when each new playground is made


    def __init__(self):
        self.updateTask = None
        self.details = "Loading" # text next to photo
        self.image = 'toontown-logo' #Main image
        self.imageTxt = 'Toontown Galaxy' #Hover text for main image 
        self.smallLogo = 'discord-icon' #small image in corner
        self.state = '   ' #Displayed underneath details, used for boarding groups
        self.smallTxt = 'Loading'
        self.partySize = 1
        self.maxParty = 1

    def stopBoarding(self):
        self.partySize = 1
        self.state = ''
        self.maxParty = 1
        self.setData()

    def allowBoarding(self, size):
        self.state = 'In a boarding group'
        self.partySize = 1
        self.maxParty = size
        self.setData()

    def setBoarding(self, size):
        self.PartySize = size
        self.setData()

    def setData(self):
        details = self.details
        image = self.image
        imageTxt = self.imageTxt
        smallLogo = self.smallLogo
        smallTxt = self.smallTxt
        state = self.state
        party = self.partySize
        maxSize = self.maxParty
        RPC.update(state=state,details=details , large_image=image, large_text=imageTxt,  small_image=smallLogo, small_text=smallTxt, party_size=[party, maxSize])

    def updateTasks(self, task):
        self.updateTask = True
        self.setData()
        return task.again
    
    def avChoice(self):
        self.image = 'toontown-logo'
        self.details = 'Picking a Toon.'
        self.setData()

    def launching(self):
        self.image = 'toontown-logo'
        self.details = 'Loading...'
        self.setData()

    def making(self):
        self.image = 'toontown-logo'
        self.details = 'Making a Toon.'

    def startTasks(self):
        taskMgr.doMethodLater(10, self.updateTasks, 'UpdateTask')

    def setDistrict(self, name):
        self.smallTxt = name
