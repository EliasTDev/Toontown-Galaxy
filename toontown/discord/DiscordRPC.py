import time 
from ctypes import *
from direct.task import Task 
from pypresence import Presence
import pypresence
clientId  = "796502813353050122"
try:
    RPC = Presence(clientId)
except:
    print("DiscordRPC: Warning : Discord not found for this client.")
    RPC = None    
try:
    RPC.connect()
except:
    print("DiscordRPC: Warning : Failed to connect to discord client.")
    RPC = None
class DiscordRPC(object):

    zone2imgdesc = { # A dict of ZoneID -> An image and a description
        1000: ["donalds-dock", "In Donald's Dock"],
        1100: ["donalds-dock", "On Barnacle Boulevard"],
        1200: ["donalds-dock", "On Seaweed Street"],
        1300: ["donalds-dock", "On Lighthouse Lane"],

        2000: ["toontown-central", "In Toontown Central"],
        2100: ["toontown-central", "On Silly Street"],
        2200: ["toontown-central", "On Loopy Lane"],
        2300: ["toontown-central", "On Punchline Place"],

        3000: ["the-brrrgh", "In The Brrrgh"],
        3100: ["the-brrrgh", "On Walrus Way"],
        3200: ["the-brrrgh", "On Sleet Street"],
        3300: ["the-brrrgh", "On Polar Place"],

        4000: ["minnies-melodyland", "In Minnie's Melodyland"],
        4100: ["minnies-melodyland", "On Alto Avenue"],
        4200: ["minnies-melodyland", "On Baritone Boulevard"],
        4300: ["minnies-melodyland", "On Tenor Terrace"],

        5000: ["daisy-gardens", "In Daisy Gardens"],
        5100: ["daisy-gardens", "On Elm Street"],
        5200: ["daisy-gardens", "On Maple Street"],
        5300: ["daisy-gardens", "On Oak Street"],

        6000: ["acorn-acres", "At Chip 'n Dale's Acorn Acres"],


        8000: ["goofy-speedway", "In Goofy Speedway"],

        9000: ["donalds-dreamland", "In Drowsy Dreamland"],
        9100: ["donalds-dreamland", "On Lullaby Lane"],
        9200: ["donalds-dreamland", "On Pajama Place"],
        9300: ["donalds-dreamland", "On Twilight Terrace"],

        10000: ["bossbot-hq", "At Bossbot HQ"],
        10100: ["bossbot-hq", "In The CEO Clubhouse"],
        10200: ["bossbot-hq", "In The CEO Clubhouse"],
        10500: ["bossbot-hq", "In The Front Three"],
        10600: ["bossbot-hq", "In The Middle Six"],
        10700: ["bossbot-hq", "In The Back Nine"],

        11000: ["sellbot-hq", "At Sellbot HQ"],
        11100: ["sellbot-hq", "In The VP Lobby"],
        11200: ["sellbot-hq", "In The Sellbot HQ Factory Exterior"],
        11500: ["sellbot-hq", "In The Sellbot Factory"],

        12000: ["cashbot-hq", "At Cashbot HQ"],
        12100: ["cashbot-hq", "In The CFO Lobby"],
        12500: ["cashbot-hq", "In The Cashbot Coin Mint"],
        12600: ["cashbot-hq", "In The Cashbot Dollar Mint"],
        12700: ["cashbot-hq", "In The Cashbot Bullion Mint"],

        13000: ["lawbot-hq", "At Lawbot HQ"],
        13100: ["lawbot-hq", "In The CJ Lobby"],
        13200: ["lawbot-hq", "In The DA's Office Lobby"],
        13300: ["lawbot-hq", "In The Lawbot Office A"],
        13400: ["lawbot-hq", "In The Lawbot Office B"],
        13500: ["lawbot-hq", "In The Lawbot Office C"],
        13600: ["lawbot-hq", "In The Lawbot Office D"],

        14000: ["tutorial", "In The Toontorial"],

        16000: ["estate", "At A Toon Estate"],

        17000: ['golf', "In Chip 'n Dale's MiniGolf"],

        18000: ["party", "At A Toon Party"],
    }

    def __init__(self):
        self.updateTask = None
        self.details = "Loading" # text next to photo
        self.image = 'toontown-logo' #Main image
        self.imageTxt = 'Toontown: Galaxy' #Hover text for main image 
        self.smallLogo = 'discord-icon' #small image in corner
        self.state = '   ' #Displayed underneath details, used for boarding groups
        self.smallTxt = 'Loading'
        self.partySize = 1
        self.maxParty = 1

    def stopBoarding(self):
        self.partySize = 1
        self.state = '  '
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

    def setData(self, details=None, image=None, imageTxt=None):
        if details == None:
            details = self.details
        if image == None:
            image = self.image
        if imageTxt == None:
            imageTxt = self.imageTxt
        smallLogo = self.smallLogo
        smallTxt = self.smallTxt
        state = self.state
        party = self.partySize
        maxSize = self.maxParty
        if RPC is not None:
            try:
                RPC.update(state=state,details=details , large_image=image, large_text=imageTxt,  small_image=smallLogo, small_text=smallTxt, party_size=[party, maxSize])
            except pypresence.exceptions.InvalidID:
                self.notify.warning("Discord client is gone")
    def setLaff(self, hp, maxHp):
        self.state = '{0}: {1}/{2}'.format(base.localAvatar.name, hp, maxHp)
        self.setData()


    def updateTasks(self, task):
        self.updateTask = True
        self.setData()
        return task.again
    
    def avChoice(self):
        self.image = 'toontown-logo'
        self.details = 'Picking a Toon.'
        self.state = '  '
        self.setData()

    def launching(self):
        self.image = 'toontown-logo'
        self.details = 'Loading...'
        self.setData()

    def making(self):
        self.image = 'toontown-logo'
        self.details = 'Making a Toon.'

    def vp(self):
        self.image = 'vp'
        self.details = 'Fighting the vp.'
        self.setData()

    def cfo(self):
        self.image = 'cfo'
        self.details = 'Fighting the cfo.'
        self.setData()

    def cj(self):
        self.image = 'cj'
        self.details = 'Fighting the cj.'
        self.setData()

    def ceo(self):
        self.image = 'ceo'
        self.details = 'Fighting the ceo.'

    def suitBuilding(self):
        #TODO need an image for this
        self.details = 'In a Cog Building'
        self.image = 'toontown-logo'

    def endlessBuilding(self):
        #TODO need an image for this
        #self.details = 'In The Infini-Suite'
        self.details = '???'
        self.image = 'toontown-logo'
    def startTasks(self):
        taskMgr.doMethodLater(10, self.updateTasks, 'UpdateTask')

    def setDistrict(self, name):
        self.smallTxt = name

    def setZone(self,zone): # Set image and text based on the zone
        if not isinstance(zone, int):
            return
        zone -= zone % 100
        data = self.zone2imgdesc.get(zone,None)
        if data:
            self.image = data[0]
            self.details = data[1]
            self.setData()
        else:
            print("Error: Zone Not Found!")

