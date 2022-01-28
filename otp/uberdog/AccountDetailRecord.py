
from otp.otpbase import OTPGlobals


class SubDetailRecord:
    def __init__(self):
        self.subId = 0
        self.subOwnerId = 0
        self.subName = ''
        self.subActive = ''
        self.subAccess = ''
        self.subLevel = 0
        self.subNumAvatars = 0
        self.subNumConcur = 0
        self.subFounder = 0

    def __str__(self):
        s = ''
        s += "========== Sub %d ==========\n" % (self.subId)
        s += "Sub Id: %d\n" % (self.subId)
        s += "Sub Owner Id: %d\n" % (self.subOwnerId)
        s += f"Sub Name: {self.subName}\n"
        s += f"Sub Active: {self.subActive}\n"
        s += f"Sub Access: {self.subAccess}\n"
        s += "Sub Level: %d\n" % (self.subLevel)
        s += "Sub MaxAvatars: %d\n" % (self.subNumAvatars)
        s += "Sub Concurrent: %d\n" % (self.subNumConcur)
        s += "Sub Founder: %d\n" % (self.subFounder)
        return s


class AccountDetailRecord:
    def __init__(self):
        self.openChatEnabled = False
        self.createFriendsWithChat = False
        self.chatCodeCreation = False
        self.piratesAccess = OTPGlobals.AccessUnknown
        self.familyAccountId = 0
        self.playerAccountId = 0
        self.playerName = ''
        self.playerNameApproved = False
        self.maxAvatars = 0
        self.numFamilyMembers = 0
        self.familyMembers = []
        self.numSubs = 0
        self.subDetails = {}
        self.maxAvatarSlots = 0
        self.WLChatEnabled = False

    def getMaxNumAvatars(self, subId):
        subDetails = self.subDetails.get(subId)
        if subDetails:
            return subDetails.subNumAvatars
        else:
            return 0

    def canOpenChatAndNotGetBooted(self):
        return self.openChatEnabled or self.createFriendsWithChat

    def __str__(self):
        s = f'========== Account {self.playerAccountId} ==========\n'
        s += f"OpenChatEnabled: {self.openChatEnabled}\n"
        s += f"WLChatEnabled: {self.WLChatEnabled}\n"
        s += f"CreateFriendsWithChat: {self.createFriendsWithChat}\n"
        s += f"ChatCodeCreation: {self.chatCodeCreation}\n"
        s += f"PiratesAccess: {self.piratesAccess}\n"
        s += "FamilyAccountId: %d\n" % self.familyAccountId
        s += "PlayerAccountId: %d\n" % self.playerAccountId
        s += f"PlayerName: {self.playerName}\n"
        s += "AccountNameApproved: %d\n" % self.playerNameApproved
        s += "MaxAvatars: %d\n" % self.maxAvatars
        s += "MaxAvatarSlots: %d\n" % self.maxAvatarSlots
        s += "NumFamilyMembers: %d\n" % self.numFamilyMembers
        s += f"FamilyMembers: {self.familyMembers}\n"
        s += f"NumSubs: {self.numSubs}\n"
        for subDetails in list(self.subDetails.values()):
            s += str(subDetails)
        s += '================================\n'
        return s
