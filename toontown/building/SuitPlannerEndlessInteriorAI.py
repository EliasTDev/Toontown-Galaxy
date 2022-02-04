
# This is the pain file :D

""" SuitPlannerEndlessInteriorAI module:  contains the SuitPlannerEndlessInteriorAI
    class which handles management of all suits within a endless suit building."""
import random
from toontown.suit import SuitDNA
from direct.directnotify import DirectNotifyGlobal
from toontown.suit import DistributedSuitAI
import types, functools
from otp.ai.AIBaseGlobal import *

from . import SuitPlannerInteriorAI


class SuitPlannerEndlessInteriorAI(SuitPlannerInteriorAI.SuitPlannerInteriorAI):
    SUIT_TRACKS = ['s', 'm', 'l', 'c']
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'SuitPlannerInteriorAI')

    def __init__(self, zone):
        self.dbg_4SuitsPerFloor = config.GetBool("4-suits-per-floor", 0)
        self.dbg_1SuitPerFloor = config.GetBool("1-suit-per-floor", 0)  # formerly called 'wuss-suits'

        self.zoneId = zone
        self.numFloors = float('inf')

        # By default, if an invasion is in progress we only generate
        # suits of that kind.  Set this false to turn off this
        # behavior.
        self.respectInvasions = False

        # This dbg var forces the creations of all 1 suit type (overrides level/type restrictions)
        dbg_defaultSuitName = simbase.config.GetString('suit-type', 'random')
        if (dbg_defaultSuitName == 'random'):
            self.dbg_defaultSuitType = None
        else:
            self.dbg_defaultSuitType = SuitDNA.getSuitType(dbg_defaultSuitName)

        #self._genSuitInfos()
        assert (len(self.suitInfos) > 0)

    def _genSuitInfos( self, currFloor):
        """
        // Function:   create information about all suits that will exist
        //             in this building
        // Parameters: numFloors, number of floors in the building
        //             bldgLevel, how difficult the building is, based on
        //                        the suit that initially took the building
        //             bldgTrack, the track of the building, based on the
        //                        track that initially took the building
        // Changes:
        """
        self.suitInfos = []




        # process each floor in the building and create all active and
        # reserve suits
        #
        infoDict = {}
        lvls = self.__genLevelList(currFloor)

        # now randomly decide how many suits will be active and how
        # many will be in reserve, create the active suit objects
        # create the active suits in order of highest level to lowest
        # this is only because we want to make sure the highest level
        # active suit is in the first position in the list
        #
        activeDicts = []

        if (self.dbg_4SuitsPerFloor):
            numActive = 4
        else:
            numActive = random.randint( 1, min( 4, len( lvls ) ) )

        if (currFloor + 1) %4 == 0 and len(lvls) > 1:
            # Make the boss be suit 1 (unless there is only 1 active suit)
            origBossSpot = len(lvls) - 1
            if (numActive == 1):
                newBossSpot = numActive - 1
            else:
                newBossSpot = numActive - 2
            tmp = lvls[newBossSpot]
            lvls[newBossSpot] = lvls[origBossSpot]
            lvls[origBossSpot] = tmp

           # bldgInfo = SuitBuildingGlobals.SuitBuildingInfo[ bldgLevel ]

            for currActive in range( numActive - 1, -1, -1 ):
                level = lvls[ currActive ]
                _type = self.__genNormalSuitType( level )
                activeDict = {}
                activeDict['type'] = _type
                #activeDict['track']
                activeDict['level'] = level
                activeDict['revives'] = revives
                activeDicts.append(activeDict)
            infoDict['activeSuits'] = activeDicts

            # now create the reserve suit objects, also assign each a
            # % join restriction, this indicates when the reserve suit
            # should join the battle based on how much damage has been
            # done to the suits currently in the battle
            #
            reserveDicts = []
            numReserve = len( lvls ) - numActive
            joinChances = self.__genJoinChances( numReserve )
            for currReserve in range( numReserve ):
                level = lvls[ currReserve + numActive ]
                _type = self.__genNormalSuitType(  )
                reserveDict = {}
                reserveDict['type'] = type
               # reserveDict['track'] = bldgTrack
                reserveDict['level'] = level
                reserveDict['revives'] = revives
                reserveDict['joinChance'] = joinChances[currReserve]
                reserveDicts.append(reserveDict)
            infoDict['reserveSuits'] = reserveDicts

            self.suitInfos.append(infoDict)

        #self.print()

    def __genNormalSuitType( self, lvl ):
        """
        // Function:   generate info for a normal suit that we might find
        //             in this particular building
        // Parameters: none
        // Changes:
        // Returns:    list containing the suit level, type, and track
        """
        # there is a similar formula in DistributedSuitPlannerAI used for
        # picking suit types for the streets, based on the suit level we
        # need to make sure we pick a valid suit type that can actually
        # be this level (each suit type can be 1 of 5 levels)
        #
        # TODO: track this formula down and make it use
        # SuitDNA.getRandomSuitType

        if (self.dbg_defaultSuitType is not None):
            return self.dbg_defaultSuitType

        return SuitDNA.getRandomSuitType(lvl)

    def __genLevelList( self, currFloor):
        """
        // Function:   based on a few parameters from the building, create
        //             a list of suit levels for a specific floor
        // Parameters: bldgLevel, the level of the current building (the
        //                        level of the suit that took it over, this
        //                        value is 0-based)
        //             currFloor, the current floor that we are calculating
        //             numFloors, the total number of floors in this bldg
        // Changes:
        // returns:    list of suit levels
        """



        # For quick building battles during debug.
        if (self.dbg_1SuitPerFloor):
            return [1]    # 1 suit of max level 1
        elif (self.dbg_4SuitsPerFloor):
            return [5,6,7,10]  # a typical level with a higher level boss (must be at end)
        # TODO change this to how we want to envision the level pool range
        lvlPoolRange = [currFloor, currFloor + 5]
        #maxFloors =  bldgInfo[ SuitBuildingGlobals.SUIT_BLDG_INFO_FLOORS ][1]

        # now figure out which level pool multiplier to use
        #
        # For now we use 1x  #TODO figure this one out too (what we want to change it to )
        lvlPoolMults = [1]
        floorIdx = currFloor

        # now adjust the min and max level pool range based on the multipliers
        # we just got
        #
        lvlPoolMin = lvlPoolRange[ 0 ] * lvlPoolMults[ floorIdx ]
        lvlPoolMax = lvlPoolRange[ 1 ] * lvlPoolMults[ floorIdx ]

        # now randomly choose a level pool between the max and min
        #
        lvlPool = random.randint( int(lvlPoolMin), int(lvlPoolMax) )

        # find the min and max possible suit levels that we can create
        # for this level of building
        #
        lvlMin = 1
        #lvlMax = float('inf')

        # now randomly generate levels within our min and max, pulling
        # from our pool until we run out
        #
        self.notify.debug( "Level Pool: " + str( lvlPool ) )
        lvlList = []
        while lvlPool >= lvlMin:
            newLvl =  random.randint( lvlMin, lvlPool )
            lvlList.append( newLvl )
            lvlPool -= newLvl

        # now if we are on the top floor of the building, make sure to
        # add in a slot for the building boss
        #
        if currFloor + 1 % 4 == 0:
            # TODO this is a place holder formula for now
            bossLvlRange=[(currFloor *2 ) / 4,(currFloor *2 ) / 4 ]
            newLvl = random.randint( bossLvlRange[ 0 ], bossLvlRange[ 1 ] )
            lvlList.append( newLvl )


        lvlList.sort(key=functools.cmp_to_key(cmp))
        self.notify.debug( "LevelList: " + repr( lvlList ) )
        return lvlList

    def __setupSuitInfo( self, suit, suitLevel, suitType ):
        """
        create dna information for the given suit with the given track
        and suit type
        """

        dna = SuitDNA.SuitDNA()
        randomTrackChosen = random.choice(self.SUIT_TRACKS)
        dna.newSuitRandom(suitType, randomTrackChosen)
        suit.dna = dna
        self.notify.debug("Creating suit type " + suit.dna.name +
                          " of level " + str( suitLevel ) +
                          " from type " + str( suitType ) +
                          " and track " + str( randomTrackChosen ) )
        suit.setLevel( suitLevel )
        skeleton = random.choice([True, False])
        # We can't make a suit a skeleton until after generate.
        # Pass this info back so we know whether to do it or not
        return skeleton

    def __genSuitObject(self, suitZone, suitType, suitLevel, revives = 0):
        """
        // Function:   generate a distributed suit object
        // Parameters:
        // Changes:
        // Returns:    the suit object created
        """
        newSuit = DistributedSuitAI.DistributedSuitAI( simbase.air, None )
        skel = self.__setupSuitInfo( newSuit, suitLevel, suitType )
        if skel:
            newSuit.setSkelecog(1)
        newSuit.setSkeleRevives(revives)
        newSuit.generateWithRequired( suitZone )

        # Fill in the name so we can tell one suit from another in printouts.
        newSuit.node().setName('suit-%s' % (newSuit.doId))
        return newSuit

    def myPrint(self):
        """
        Overidden as it will break the game trying to get information about every floor possible
        """
        return

    def genFloorSuits(self, floor):
        """
        """
        self.notify.debug('generating suits for floor: %d' % floor)
        suitHandles = {}
        floorInfo = self.suitInfos[floor]

        activeSuits = []
        for activeSuitInfo in floorInfo['activeSuits']:
            suit = self.__genSuitObject(self.zoneId,
                                activeSuitInfo['type'],
                                #activeSuitInfo['track'],
                                activeSuitInfo['level'],
                                activeSuitInfo['revives'])

            activeSuits.append(suit)
       # assert(len(activeSuits) > 0)
        suitHandles['activeSuits'] = activeSuits

        reserveSuits = []
        for reserveSuitInfo in floorInfo['reserveSuits']:
            suit = self.__genSuitObject(self.zoneId,
                                reserveSuitInfo['type'],
                                #reserveSuitInfo['track'],
                                reserveSuitInfo['level'],
                                reserveSuitInfo['revives'])
            reserveSuits.append((suit, reserveSuitInfo['joinChance']))
        suitHandles['reserveSuits'] = reserveSuits

        return suitHandles

    def genSuits(self, currentFloor):
        # Call this function on each floor before the elevator movie finishes to generate the suits on that floor
        floorSuitHandles = self.genFloorSuits(currentFloor)
        suitHandles.append(floorSuitHandles)
        return suitHandles
