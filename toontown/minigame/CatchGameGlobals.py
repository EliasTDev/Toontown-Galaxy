# CatchGameGlobals.py: contains catch game stuff
# used by both AI and client

EndlessGame = config.GetBool('endless-catch-game', 0)

#GameDuration = 60.
# this is the duration of the tag game music...
GameDuration = 55.

# this class is purely for syntactic convenience;
# with it, we can reference properties of drop object types by name
# 'name' == name of the drop object
# 'good' == is this a good thing to catch
# onscreenDurMult is how many times longer the object should take to fall,
#   once on-screen, than baseline objects (durationMult==1.)
#   For instance, an object type with an onscreenDurMult of .5 will be
#   on-screen half as long as a baseline object.


class DropObject:
    def __init__(self, name, good, onscreenDurMult, modelPath):
        self.name = name
        self.good = good
        self.onscreenDurMult = onscreenDurMult
        self.modelPath = modelPath

    def isBaseline(self):
        return (self.onscreenDurMult == 1.)


# definitions of drop types, in arbitrary order
DropObjectTypes = [
    # order is not important
    DropObject('apple', 1, 1., 'phase_4/models/minigames/apple'),
    DropObject('orange', 1, 1., 'phase_4/models/minigames/orange'),
    DropObject('pear', 1, 1., 'phase_4/models/minigames/pear'),
    DropObject('coconut', 1, 1., 'phase_4/models/minigames/coconut'),
    DropObject('watermelon', 1, 1., 'phase_4/models/minigames/watermelon'),
    DropObject('pineapple', 1, 1., 'phase_4/models/minigames/pineapple'),
    DropObject('anvil', 0, .4, 'phase_4/models/props/anvil-mod'),
]

# index into Name2DropObjectType by object name, then access named properties
# (see class DropObject above for property names)
Name2DropObjectType = {}
for type in DropObjectTypes:
    Name2DropObjectType[type.name] = type

# for transmitting drop-object types over the network, it's more efficient
# to be sending a number (DOTypeId) than a string.
#
# Name2DOTypeId and DOTypeId2Name map between name strings
# and typeIds:
#   Name2DOTypeId['apple'] == some number
#   DOTypeId2Name[some number] == 'apple'
Name2DOTypeId = {}
names = sorted(Name2DropObjectType.keys())
for i in range(len(names)):
    Name2DOTypeId[names[i]] = i
# our sorted list of names just happens to be the typeId->name table
DOTypeId2Name = names

"""
import CatchGameGlobals
for np in range(4):
    for sz in (2000,1000,5000,4000,3000,9000):
        numFruits = CatchGameGlobals.NumFruits[np][sz]
        jb = int(int(numFruits / 2) + round(numFruits / 4.))
        print '%s: %s: %s' % (np, sz, jb)
"""
# this is for the AI, so it doesn't have to do calculations, and so the
# client code can calculate these values in a straightforward manner.
# index by numToons-1, then safezone ID
# THIS TABLE WAS GENERATED BY DistributedCatchGame.py; DO NOT EDIT
NumFruits = [
    # 1 player
    {2000: 18, 1000: 19, 5000: 22, 4000: 24, 3000: 27, 9000: 28, },
    # 2 players
    {2000: 30, 1000: 33, 5000: 38, 4000: 42, 3000: 46, 9000: 50, },
    # 3 players
    {2000: 42, 1000: 48, 5000: 54, 4000: 60, 3000: 66, 9000: 71, },
    # 4 players
    {2000: 56, 1000: 63, 5000: 70, 4000: 78, 3000: 85, 9000: 92, },
]
