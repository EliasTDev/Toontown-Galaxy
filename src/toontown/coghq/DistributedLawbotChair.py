from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.fsm import FSM
from direct.distributed import DistributedObject
from direct.showutil import Rope
from direct.showbase import PythonUtil
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from direct.actor import Actor
from toontown.suit import Suit
from toontown.suit import SuitDNA
import random
from toontown.battle import BattleProps
from toontown.toon import NPCToons

class DistributedLawbotChair(DistributedObject.DistributedObject, FSM.FSM):
    """ This class represents a crane holding a magnet on a cable.
    The DistributedCashbotBoss creates four of these for the CFO
    battle scene. """

    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLawbotChair')

    chairCushionSurface = Point3(0, -0.75, 2.25)
    landingPt = Point3(0, -1.5, 0)    
    courtroomCeiling = 30
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedLawbotBossChair')

        self.boss = None
        self.index = None
        self.avId = 0
        
        #self.modelPath = "phase_5.5/models/estate/chairAdesat"
        self.modelPath = "phase_11/models/lawbotHQ/JuryBoxChair"        
        self.modelFindString = None

        self.nodePath = None

        self.ival = None
        self.origHpr = Point3(0,0,0)
        self.downTime = 0.5 #how long to stomp down
        self.upTime = 5 #how long to go up

        self.cogJuror = None
        self.propInSound = None
        self.propOutSound = None
        self.propTrack = None
        self.cogJurorTrack = None
        self.cogJurorSound = None

        self.toonJurorIndex = -1
        self.toonJuror = None
        

    def announceGenerate(self):
        self.notify.debug("announceGenerate: %s" % self.doId)
        DistributedObject.DistributedObject.announceGenerate(self)
        self.name = 'Chair-%s' % (self.doId)
        #self.setName(self.name)

  

        # Load the model, (using loadModelOnce), and child it to the nodepath
        self.loadModel(self.modelPath, self.modelFindString)
        # animate if necessary
        #self.startAnimation()


        # Set up random generator
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.doId)
        
        self.loadSounds()
        self.loadCogJuror()
        self.cogJuror.stash()


        
        #tempTuple = ToontownGlobals.LawbotBossChairPosHprs[self.index]        
        #self.nodePath.setPosHpr(*tempTuple)
        #self.origHpr = Point3( tempTuple[3], tempTuple[4], tempTuple[5])

        origPos = self.computePos()
        self.nodePath.setPos(origPos)
        self.nodePath.setHpr(-90,0,0)

        #self.downTime = ToontownGlobals.LawbotBossChairTimes[self.index][0]
        #self.upTime = ToontownGlobals.LawbotBossChairTimes[self.index][1]
        #self.stayDownTime = ToontownGlobals.LawbotBossChairTimes[self.index][2]

        # Put this thing in the world
        #self.nodePath.wrtReparentTo(render)
        chairParent = self.boss.getChairParent()
        self.nodePath.wrtReparentTo(chairParent)

        
        assert(self.index not in self.boss.chairs)
        self.boss.chairs[self.index] = self

        

    def delete(self):
        # Call up the chain
        DistributedObject.DistributedObject.delete(self)

        # Really, we don't want to unloadModel on this, until we're
        # leaving the safezone.  Calling unloadModel will force the
        # next treasure of this type to reload from disk.
        loader.unloadModel(self.modelPath)

        self.unloadSounds()
        self.nodePath.removeNode()


    def loadModel(self, modelPath, modelFindString = None):
        if self.nodePath == None:
            self.makeNodePath()
        else:
            self.chair.getChildren().detach()

        # Load the chair model and put it under our root node.
        model = loader.loadModel(modelPath)
        if modelFindString != None:
            model = model.find("**/" + modelFindString)
            assert model != None

        model.instanceTo(self.chair)

        #hide the default collision info,
        trigger_chair = self.chair.find('**/trigger_chair')
        if not trigger_chair.isEmpty():
            trigger_chair.stash()

        collision_chair = self.chair.find('**/collision_chair')
        if not collision_chair.isEmpty():            
            collision_chair.stash()

        #hide the shadow, it looks wrong, bring it back if there's something solid under the chair
        shadow = self.chair.find('**/shadow')
        if not shadow.isEmpty():
            #shadow.stash()
            pass
        
        self.scale = 0.5
        self.chair.setScale(self.scale)

        self.attachColSphere()

    

    def loadSounds(self):
        if self.propInSound == None:
            self.propInSound = base.loader.loadSfx("phase_5/audio/sfx/ENC_propeller_in.mp3")
        if self.propOutSound == None:
            self.propOutSound = base.loader.loadSfx("phase_5/audio/sfx/ENC_propeller_out.mp3")
        if self.cogJurorSound == None:
            self.cogJurorSound = base.loader.loadSfx("phase_11/audio/sfx/LB_cog_jury.mp3")

    def unloadSounds(self):
        if self.propInSound:
            del self.propInSound
            self.propInSound = None
        if self.propOutSound:
            del self.propOutSound
            self.propOutSound = None
        if self.cogJurorSound:
            del self.cogJurorSound
            self.cogJurorSound = None
        
        

    def loadCogJuror(self):
        self.cleanupCogJuror()
        self.cogJuror = Suit.Suit()

        #level = random.randrange(len(SuitDNA.suitsPerLevel))
        level = self.randomGenerator.randrange(len(SuitDNA.suitsPerLevel))

            # And a random type to match the level.
        self.cogJuror.dna = SuitDNA.SuitDNA()

        #level = 1
        self.cogJuror.dna.newSuitRandom(level = level, dept = 'l')

        self.cogJuror.setDNA(self.cogJuror.dna)

        self.cogJuror.pose('landing',0)
        #self.cogJuror.pose('neutral',0)
        self.cogJuror.reparentTo(self.nodePath)
 
            

        # now create info for the propeller's animation
        #
        self.cogJuror.prop = None
        if self.cogJuror.prop == None:
            self.cogJuror.prop = BattleProps.globalPropPool.getProp('propeller')

        head = self.cogJuror.find("**/joint_head")
        self.cogJuror.prop.reparentTo(head)
        
        self.propTrack = Sequence(
            ActorInterval(self.cogJuror.prop, 'propeller',
                          startFrame = 8,
                          endFrame = 25,
                          ),
            )



        #self.propTrack.loop()
        
    def attachColSphere(self):

        chairTop = self.nodePath.find("**/top*")
        chairHandle = self.nodePath.find("**/handle*")

        collNode = CollisionNode(self.uniqueName("headSphere"))
        #collNode.setIntoCollideMask(WallBitmask)
        #collNode.addSolid(collSphere)

        topBounds = self.chair.getBounds()
        center = topBounds.getCenter()
        radius = topBounds.getRadius()

        #radius is a bit too big, scale it down a little
        radius *= 0.65
        adjustedZ = center[2] 
        adjustedZ += 0.6
        
        sphere1 = CollisionSphere(center[0], center[1], adjustedZ, radius)
        sphere1.setTangible(1)    #we want it tangible
        collNode.addSolid(sphere1)
        #collNode.setTag('attackCode', str(ToontownGlobals.BossCogChairStomp))        
        collNode.setName('Chair-%s'% self.index)

        
        self.collNodePath = self.nodePath.attachNewNode(collNode)
        #self.collNodePath.stash()


    def makeNodePath(self):
        self.nodePath = Actor.Actor() #NodePath(self.uniqueName("chairNodePath"))        

        self.chair = self.nodePath.attachNewNode('myChair')

    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        assert(self.boss.chairs.get(self.index) == self)

        
        self.nodePath.detachNode()
        if (self.ival):        
            self.ival.finish();
            self.ival = None

        self.ignoreAll()
        del self.boss.chairs[self.index]
        self.cleanup()

        if self.propTrack:
            self.propTrack.finish()
            self.propTrack = None

        if self.cogJurorTrack:
            self.cogJurorTrack.finish()
            self.cogJurorTrack = None
            
        self.cleanupCogJuror()
        self.cleanupToonJuror()

    def stopCogsFlying(self):
        if self.ival:        
            self.ival.finish();
            self.ival = None

        if self.propTrack:
            self.propTrack.finish()
            self.propTrack = None

        if self.cogJurorTrack:
            self.cogJurorTrack.finish()
            self.cogJurorTrack = None

        #if not self.state == 'CogJuror':
        #    self.cleanupCogJuror()

    def cleanupCogJuror(self):
        if self.cogJuror:
            self.cogJuror.detachNode()
            self.cogJuror.delete()
            del self.cogJuror
            self.cogJuror = None
            
    def cleanupToonJuror(self):
        if self.toonJuror:
            self.toonJuror.detachNode()
            self.toonJuror.delete()
            del self.toonJuror
            self.toonJuror = None
        
        
    def cleanup(self):
        #if self.state != 'Off':
        #    self.demand('Off')
        self.boss = None

    def startCogJuror(self, duration,  y ):
        if self.cogJurorTrack:
            self.cogJurorTrack.finish()

        self.loadCogJuror()
        self.cogJuror.stash()

        x=0

        curPos = self.nodePath.getPos(render)
        z = self.courtroomCeiling - curPos[2]
        self.notify.debug('curPos =%s\nz=%f' % (curPos,z))

        
        cogTrack = Sequence(
            Func(self.cogJuror.setPos,x,y,z),
            Func(self.cogJuror.unstash),
            Func(self.propTrack.loop),
            self.cogJuror.posInterval(duration, self.landingPt, Point3(x,y,z)),
            Func(self.propTrack.finish),
            Func(self.stashCogJuror),
            #Func(self.putCogJurorOnSeat),
            )

        audioTrack = SoundInterval (self.propInSound, duration=duration, node= self.cogJuror, loop=1)

        #landingAnimTime = self.cogJuror.getDuration('landing')
        #timeToWait = duration - landingAnimTime
        #if timeToWait < 0:
        #    timeToWait = 0

        #landingTrack = Sequence(
        #    Func(self.cogJuror.pose,'landing',0),            
        #    Wait(timeToWait),
        #    Func(self.cogJuror.loop,'landing')
        #    )
        
        self.cogJurorTrack = Parallel(
            audioTrack,
            cogTrack,
            #landingTrack
            )

        self.cogJurorTrack.start()

    def stashCogJuror(self):
        if self.cogJuror and not self.cogJuror.isEmpty():
            self.cogJuror.stash()

    def putCogJurorOnSeat(self):
        self.stopCogsFlying()
        if self.cogJuror and not self.cogJuror.isEmpty():
            base.playSfx(self.cogJurorSound, node = self.chair)
            self.cogJuror.unstash()
            self.cogJuror.prop.stash()
            self.cogJuror.pose('landing',47)
            self.cogJuror.setH(180)
            self.cogJuror.setPos(0,-1.25,0.95)

            if self.toonJuror:
                self.toonJuror.hide()
        else:
            self.notify.warning('putCogJurorOnSeat invalid cogJuror')

    def putToonJurorOnSeat(self):
        if self.toonJuror and not self.toonJuror.isEmpty():
            self.toonJuror.show()
            self.toonJuror.reparentTo(self.nodePath)
            self.toonJuror.setH(180)
            self.toonJuror.setPos(0,-2.5,0.95)
            self.toonJuror.animFSM.request('Sit')            
        else:
            self.notify.warning('putToonJurorOnSeat invalid toonJuror')
            
    def showCogJurorFlying(self):
        self.notify.debug('showCogJurorFlying')
        self.startCogJuror(ToontownGlobals.LawbotBossCogJurorFlightTime, -ToontownGlobals.LawbotBossCogJurorDistance)
            


    ##### Messages To/From The Server #####

    def setBossCogId(self, bossCogId):
        self.bossCogId = bossCogId

        # This would be risky if we had toons entering the zone during
        # a battle--but since all the toons are always there from the
        # beginning, we can be confident that the BossCog has already
        # been generated by the time we receive the generate for its
        # associated battles.
        self.boss = base.cr.doId2do[bossCogId]

    def setIndex(self, index):
        self.index = index

    def setState(self, state):
        avId = 0
        if state == 'C':
            self.demand('Controlled', avId)
        elif state == 'F':
            self.demand('Free')
        elif state == 'N':
            self.demand('On')
        elif state == 'T':
            self.demand('ToonJuror')
        elif state == 'S':
            self.demand('SuitJuror')
        elif state == 'E':
            self.demand('EmptyJuror')
        elif state == 'E':
            self.demand('StopCogs')
        else:
            self.notify.error("Invalid state from AI: %s" % (state))




    def __touchedChair(self,entry):
        self.notify.debug("__touchedChair")
        self.notify.debug("self=%s entry=%s" % (self,entry))

        self.boss.touchedChair(self, entry)

    def __touchedChairHandle(self, entry):
        self.notify.debug("__touchedChairHandle")

        self.boss.touchedChairHandle(self, entry)



    ### FSM States ###


    def enterToonJuror(self):
        #make it blue
        self.chair.setColorScale(0.2,0.2,1.0,1.0)
        #import pdb; pdb.set_trace()
        self.boss.countToonJurors()

        #if self.cogJuror and self.previousState == 'CogJuror':
        #    self.cogJuror.stash()
        if not self.cogJurorTrack:
            self.cogJuror.stash()

        self.putToonJurorOnSeat()
        

    def enterSuitJuror(self):
        #make it gray
        assert self.notify.debug('enterSuitJuror')
        self.chair.setColorScale(0.5,0.5,0.5,1.0)
        self.boss.countToonJurors()
        if self.toonJuror:
            self.toonJuror.hide()
        self.putCogJurorOnSeat()

    def enterEmptyJuror(self):
        #make it white
        assert self.notify.debug('enterEmptyJuror')
        self.chair.setColorScale(1.0, 1.0, 1.0, 1.0)
        
    def enterStopCogs(self):
        assert self.notify.debug('enterStopCogs')
        self.stopCogs()

    def exitStopCogs(self):
        assert self.notify.debug('exitStopCogs, oldState=%s' % self.oldState)
        pass

    def enterOn(self):
        #do whatever we need to start the big chairs stomping
        self.notify.debug("enterOn for chair %d" % self.index)

        myHeadings = ToontownGlobals.LawbotBossChairHeadings[self.index]

        seqName = "LawbotBossChair-%s" % self.doId
        self.ival = Sequence(name = seqName)
        downAngle = -80

        for index in range(len(myHeadings)):
            nextIndex = index +1;
            if (nextIndex == len(myHeadings)):
                nextIndex = 0
                
            goingDown = self.nodePath.hprInterval(self.downTime,
                                                  Point3(myHeadings[index] + self.origHpr[0],
                                                  downAngle,
                                                  self.origHpr[2]),
                                                  startHpr = Point3(myHeadings[index] + self.origHpr[0] ,0,self.origHpr[2]))
            self.ival.append(goingDown)
            self.ival.append(Wait(self.stayDownTime))
            
            goingUp = self.nodePath.hprInterval(self.upTime,
                                                Point3(myHeadings[nextIndex] + self.origHpr[0],
                                                0,
                                                self.origHpr[2]),
                                                startHpr = Point3(myHeadings[index] + self.origHpr[0], downAngle, self.origHpr[2]))
            self.ival.append(goingUp)
            

        self.ival.loop() #globalClock.getFrameTime());
        self.accept('enterChairZap', self.__touchedChair)
        self.accept('enterChairHandleZap', self.__touchedChairHandle)


    def computePos(self):
        rowIndex = self.index % 6
        if self.index < 6:
            startPt = Point3(*ToontownGlobals.LawbotBossChairRow1PosA)
            endPt = Point3(*ToontownGlobals.LawbotBossChairRow1PosB)
        else:
            startPt = Point3(*ToontownGlobals.LawbotBossChairRow2PosA)
            endPt = Point3(*ToontownGlobals.LawbotBossChairRow2PosB)
            
        totalDisplacement = endPt - startPt
        stepDisplacement = totalDisplacement / ( 6-1 )

        newPos = stepDisplacement * rowIndex
        self.notify.debug('curDisplacement = %s' % newPos)
        newPos += startPt
        self.notify.debug('newPos before offset  = %s' % newPos)

        #since we show the chairs now at the very start, offset it
        newPos -= Point3(*ToontownGlobals.LawbotBossJuryBoxRelativeEndPos)
        self.notify.debug('newPos  = %s' % newPos)        
        return newPos

    def loadToonJuror(self):
        self.cleanupToonJuror()        
        self.toonJuror = NPCToons.createLocalNPC(ToontownGlobals.LawbotBossBaseJurorNpcId + self.toonJurorIndex)
        self.toonJuror.hide()
        pass
    
            
    def setToonJurorIndex(self, newVal):
        if not self.toonJurorIndex == newVal:
            self.toonJurorIndex = newVal
            self.loadToonJuror()

            
