"""
Stores the constants relating to controls that cant be stored in toontownglobals due to import conflicts
"""
from toontown.toonbase import ToontownGlobals
#Get hotkey name for moving forward
MOVE_FORWARD = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyUp))
#Get hotkey name for moving backwards
MOVE_BACKWARDS = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyDown))
#Get hotkey name for moving left

MOVE_LEFT = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyLeft))
#Get hotkey name for moving right
MOVE_RIGHT = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyRight))
#get hotkey name for jumping
JUMP = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyJump))
#Get hotkey name for throwing an object in a boss fight 
THROW = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeyThrow))
#Get hotkey for sprinting 
SPRINT = str(base.controlManager.getKeyName("movement", ToontownGlobals.HotkeySprint))
#Get hotkey for opening the shticker book
BOOK = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyBook)
#Get hotkey for opening tasks
TASKS = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyTasks)
#Get hotkey for closing tasks
#Get hotkey for opening inventory
INVENTORY = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyInventory)
#Get hotkey for closing inventory
#Get hotkey for opening friends gui
FRIENDS = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyFriends) #What friends XD
#Get hotkey for opening the street map
STREET_MAP = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyMap) 
#Get hotkey for closing the street map
#Get hotkey for taking a screenshot
SCREENSHOT = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyScreenshot)
#Get hotkey for opening the speedchat plus gui
CHAT = base.controlManager.getKeyName("interaction", ToontownGlobals.HotkeyChat)