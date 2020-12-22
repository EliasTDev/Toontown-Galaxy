from .AIBaseGlobal import *
from pandac.PandaModules import *
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPGlobals
from direct.showbase import PythonUtil, GarbageReport, ContainerReport, MessengerLeakDetector
from direct.showbase import ContainerLeakDetector
from direct.showbase.PythonUtil import Functor, DelayedCall, formatTimeCompact
#import fpformat
import string
import time
import re
from direct.task import Task
from toontown.shtiker import CogPageGlobals
from toontown.coghq import CogDisguiseGlobals
from toontown.fishing import FishGlobals
from toontown.golf import GolfGlobals
from toontown.quest import Quests
from toontown.racing import RaceGlobals
from toontown.suit import SuitDNA
from toontown.toon import Experience
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase.PythonUtil import *
from toontown.racing.KartDNA import KartDict
from toontown.cogdominium import CogdoFlyingGameGlobals

class MagicWordManagerAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("MagicWordManagerAI")

    supportSuperchat = simbase.config.GetBool('support-superchat', 0)
    supportRename = simbase.config.GetBool('support-rename', 0)

    # Fill in by subclass
    GameAvatarClass = None

    # This will hold the local namespace we evaluate '~ai' messages
    # within.
    ExecNamespace = { }

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

    def setMagicWord(self, word, avId, zoneId, signature):
        senderId = self.air.getAvatarIdFromSender()

        sender = self.air.doId2do.get(senderId, None)
        if sender:
            if senderId == avId:
                sender = "%s/%s(%s)" % (sender.accountName, sender.name, senderId)
            else:
                sender = "%s/%s(%s) (for %d)" % (sender.accountName, sender.name, senderId, avId)
        else:
            sender = "Unknown avatar %d" % (senderId)

        self.notify.info("%s (%s) just said the magic word: %s" % (sender, signature, word))
        self.air.writeServerEvent('magic-word', senderId, "%s|%s|%s" % (sender, signature, word))
        if avId in self.air.doId2do:
            av = self.air.doId2do[avId]

            try:
                self.doMagicWord(word, av, zoneId, senderId)
            except:
                response = describeException(backTrace = 1)
                self.notify.warning("Ignoring error in magic word:\n%s" % response)
                self.down_setMagicWordResponse(senderId, response)
        else:
            self.notify.info("Don't know avatar %d." % (avId))

    def wordIs(self, word, w):
        return word == w or word[:(len(w)+1)] == ('%s ' % w)

    def getWordIs(self, word):
        # bind a word to self.wordIs and return a callable obj
        return Functor(self.wordIs, word)

    def doMagicWord(self, word, av, zoneId, senderId):
        return 
        """
        wordIs = self.getWordIs(word)








 


        elif wordIs('~ai'):
            # Execute an arbitrary Python command on the AI.
            command = word[3:].strip()
            self.notify.warning("Executing command '%s' from %s" % (command, senderId))
            text = self.__execMessage(command)[:simbase.config.GetInt("ai-debug-length",300)]
            self.down_setMagicWordResponse(
                senderId, text)

        elif wordIs('~ud'):
            # Execute an arbitrary Python command on the ud.
            print(word)
            channel,command = re.match("~ud ([0-9]+) (.+)", word).groups()
            channel = int(channel)
            if(simbase.air.doId2do.get(channel)):
                self.notify.warning("Passing command '%s' to %s from %s" % (command, channel, senderId))

                try:
                    simbase.air.doId2do[channel].sendUpdate("execCommand", [command, self.doId, senderId, zoneId])
                except:
                    pass



        elif wordIs('~aiobjecthg'):
            import gc
            objs = gc.get_objects()
            type2count = {}
            for obj in objs:
                tn = safeTypeName(obj)
                type2count.setdefault(tn, 0)
                type2count[tn] += 1
            count2type = invertDictLossless(type2count)
            counts = list(count2type.keys())
            counts.sort()
            counts.reverse()
            for count in counts:
                print('%s: %s' % (count, count2type[count]))
            self.down_setMagicWordResponse(senderId, '~aiobjecthg complete')

        elif wordIs('~aicrash'):
            # TODO: require a typed explanation in production
            # if we call notify.error directly, the magic word mgr will catch it
            # self.notify.error doesn't seem to work either
            DelayedCall(Functor(simbase.air.notify.error, '~aicrash: simulating an AI crash'))

        elif wordIs('~aicontainers'):
            args = word.split()
            limit = 30
            if 'full' in args:
                limit = None
            ContainerReport.ContainerReport('~aicontainers', log=True, limit=limit, threaded=True)

        elif wordIs('~aigarbage'):
            args = word.split()
            # it can take a LOOONG time to print out the garbage referrers and referents
            # by reference (as opposed to by number)
            full = ('full' in args)
            safeMode = ('safe' in args)
            verbose = ('verbose' in args)
            delOnly = ('delonly' in args)
            def handleGarbageDone(senderId, garbageReport):
                self.down_setMagicWordResponse(senderId, 'garbage logged, %s AI cycles' % garbageReport.getNumCycles())
            # This does a garbage collection and dumps the list of leaked (uncollectable) objects to the AI log.
            GarbageReport.GarbageReport('~aigarbage', fullReport=full, verbose=verbose, log=True, threaded=True,
                                        doneCallback=Functor(handleGarbageDone, senderId), safeMode=safeMode, delOnly=delOnly)

        elif wordIs("~creategarbage"):
            args = word.split()
            num = 1
            if len(args) > 1:
                num = int(args[1])
            GarbageReport._createGarbage(num)
            self.down_setMagicWordResponse(senderId, 'leaked garbage created')

        elif wordIs('~leaktask'):
            def leakTask(task):
                return task.cont
            taskMgr.add(leakTask, uniqueName('leakedTask'))
            leakTask = None
            self.down_setMagicWordResponse(senderId, 'leaked task created')

        elif wordIs('~aileakmessage'):
            MessengerLeakDetector._leakMessengerObject()
            self.down_setMagicWordResponse(senderId, 'messenger leak object created')

        elif wordIs('~leakContainer'):
            ContainerLeakDetector._createContainerLeak()
            self.down_setMagicWordResponse(senderId, 'leak container task created')

        elif wordIs('~aipstats'):
            args = word.split()
            hostname = None
            port = None
            if len(args) > 1:
                hostname = args[1]
            if len(args) > 2:
                port = int(args[2])
            # make sure pstats is enabled
            simbase.wantStats = 1
            Task.TaskManager.pStatsTasks = 1
            result = simbase.createStats(hostname, port)
            connectionName = '%s' % hostname
            if port is not None:
                connectionName += ':%s' % port
            if result:
                response = 'connected AI pstats to %s' % connectionName
            else:
                response = 'could not connect AI pstats to %s' % connectionName
            self.down_setMagicWordResponse(senderId, response)

        elif wordIs('~aiprofile'):
            args = word.split()
            if len(args) > 1:
                num = int(args[1])
            else:
                num = 5
            session = taskMgr.getProfileSession('~aiprofile')
            session.setLogAfterProfile(True)
            taskMgr.profileFrames(num, session)
            self.down_setMagicWordResponse(senderId, 'profiling %s AI frames...' % num)

        elif wordIs('~aiframeprofile'):
            args = word.split()
            wasOn = bool(taskMgr.getProfileFrames())
            if len(args) > 1:
                setting = bool(int(args[1]))
            else:
                setting = not wasOn
            taskMgr.setProfileFrames(setting)
            self.down_setMagicWordResponse(
                senderId,
                'AI frame profiling %s%s' % (choice(setting, 'ON', 'OFF'),
                                             choice(wasOn == setting, ' already', '')))

        elif wordIs('~aitaskprofile'):
            args = word.split()
            wasOn = bool(taskMgr.getProfileTasks())
            if len(args) > 1:
                setting = bool(int(args[1]))
            else:
                setting = not wasOn
            taskMgr.setProfileTasks(setting)
            self.down_setMagicWordResponse(
                senderId,
                'AI task profiling %s%s' % (choice(setting, 'ON', 'OFF'),
                                            choice(wasOn == setting, ' already', '')))

        elif wordIs('~aitaskspikethreshold'):
            from direct.task.TaskProfiler import TaskProfiler
            args = word.split()
            if len(args) > 1:
                threshold = float(args[1])
                response = 'AI task spike threshold set to %ss' % threshold
            else:
                threshold = TaskProfiler.GetDefaultSpikeThreshold()
                response = 'AI task spike threshold reset to %ss' % threshold
            TaskProfiler.SetSpikeThreshold(threshold)
            self.down_setMagicWordResponse(senderId, response)

        elif wordIs('~ailogtaskprofiles'):
            args = word.split()
            if len(args) > 1:
                name = args[1]
            else:
                name = None
            taskMgr.logTaskProfiles(name)
            response = 'logged AI task profiles%s' % choice(name, ' for %s' % name, '')
            self.down_setMagicWordResponse(senderId, response)

        elif wordIs('~aitaskprofileflush'):
            args = word.split()
            if len(args) > 1:
                name = args[1]
            else:
                name = None
            taskMgr.flushTaskProfiles(name)
            response = 'flushed AI task profiles%s' % choice(name, ' for %s' % name, '')
            self.down_setMagicWordResponse(senderId, response)

        elif wordIs('~aiobjectcount'):
            simbase.air.printObjectCount()
            self.down_setMagicWordResponse(senderId, 'logging AI distributed object count...')

        elif wordIs('~aitaskmgr'):
            print(taskMgr)
            self.down_setMagicWordResponse(senderId, 'logging AI taskMgr...')

        elif wordIs('~aijobmgr'):
            print(jobMgr)
            self.down_setMagicWordResponse(senderId, 'logging AI jobMgr...')

        elif wordIs('~aijobtime'):
            args = word.split()
            if len(args) > 1:
                time = float(args[1])
            else:
                time = None
            response = ''
            if time is None:
                time = jobMgr.getDefaultTimeslice()
                time = time * 1000.
                response = 'reset AI jobMgr timeslice to %s ms' % time
            else:
                response = 'set AI jobMgr timeslice to %s ms' % time
                time = time / 1000.
            jobMgr.setTimeslice(time)
            self.down_setMagicWordResponse(senderId, response)

        elif wordIs('~aidetectleaks'):
            started = self.air.startLeakDetector()
            self.down_setMagicWordResponse(senderId,
                choice(started,
                       'AI leak detector started',
                       'AI leak detector already started',
                       ))

        elif wordIs('~aitaskthreshold'):
            args = word.split()
            if len(args) > 1.:
                threshold = float(args[1])
            else:
                threshold = None
            response = ''
            if threshold is None:
                threshold = taskMgr.DefTaskDurationWarningThreshold
                response = 'reset AI task duration warning threshold to %s' % threshold
            else:
                response = 'set AI task duration warning threshold to %s' % threshold
            taskMgr.setTaskDurationWarningThreshold(threshold)
            self.down_setMagicWordResponse(senderId, response)




        elif wordIs('~aigptc'):
            args = word.split()
            if len(args) > 1. and hasattr(self.cr, 'leakDetector'):
                gptcJob = self.cr.leakDetector.getPathsToContainers(
                    '~aigptc', args[1], Functor(self._handleGPTCfinished, senderId, args[1]))
            else:
                self.down_setMagicWordResponse(senderId, 'error')

        elif wordIs('~aigptcn'):
            args = word.split()
            if len(args) > 1. and hasattr(self.cr, 'leakDetector'):
                gptcnJob = self.cr.leakDetector.getPathsToContainersNamed(
                    '~aigptcn', args[1], Functor(self._handleGPTCNfinished, senderId, args[1]))
            else:
                self.down_setMagicWordResponse(senderId, 'error')

        else:
            # The word is not an AI-side magic word.  If the sender is
            # different than the target avatar, then pass the magic
            # word down to the target client-side MagicWordManager to
            # execute a client-side magic word.
            # MPG this gets done in child class
            #if (senderId != av.doId):
            #    self.sendUpdateToAvatarId(av.doId, 'setMagicWord', [word, av.doId, zoneId])
            return 0
        return 1"""



    # MPG define in child class
    """
    def doDna(self, word, av, zoneId, senderId):
        # Handle the ~dna magic word: change your dna

        # Strip of the "~dna" part; everything else is parameters to
        # AvatarDNA.updateToonProperties.
        parms = string.strip(word[4:])

        # Get a copy of the avatar's current DNA.
        dna = ToonDNA.ToonDNA(av.dna.makeNetString())

        # Modify it according to the user's parameter selection.
        eval("dna.updateToonProperties(%s)" % (parms))

        av.b_setDNAString(dna.makeNetString())
        response = "%s" % (dna.asTuple(),)

        self.down_setMagicWordResponse(senderId, response)
    """

    def _handleGPTCfinished(self, senderId, ct, gptcJob):
        self.down_setMagicWordResponse(senderId, 'aigptc(%s) finished' % ct)

    def _handleGPTCNfinished(self, senderId, cn, gptcnJob):
        self.down_setMagicWordResponse(senderId, 'aigptcn(%s) finished' % cn)

    def __execMessage(self, message):
        if not self.ExecNamespace:
            # Import some useful variables into the ExecNamespace initially.
            exec('from pandac.PandaModules import *', globals(), self.ExecNamespace)
            #self.importExecNamespace()

        # Now try to evaluate the expression using ChatInputNormal.ExecNamespace as
        # the local namespace.
        try:
            return str(eval(message, globals(), self.ExecNamespace))

        except SyntaxError:
            # Maybe it's only a statement, like "x = 1", or
            # "import math".  These aren't expressions, so eval()
            # fails, but they can be exec'ed.
            try:
                exec(message, globals(), self.ExecNamespace)
                return 'ok'
            except:
                exception = sys.exc_info()[0]
                extraInfo = sys.exc_info()[1]
                if extraInfo:
                    return str(extraInfo)
                else:
                    return str(exception)
        except:
            exception = sys.exc_info()[0]
            extraInfo = sys.exc_info()[1]
            if extraInfo:
                return str(extraInfo)
            else:
                return str(exception)

    def down_setMagicWordResponse(self, avId, response):
        """down_setMagicWordResponse(self, avId, string response)

        Send a response to the avatar who said the magic word.
        """
        self.sendUpdateToAvatarId(avId, 'setMagicWordResponse', [response])

    def setWho(self, avIds):
        # Sent by the client in response to ~who.
        str = ''
        for avId in avIds:
            obj = self.air.doId2do.get(avId, None)
            if not obj:
                self.air.writeServerEvent('suspicious', avId, 'MagicWordManager.setWho not a valid avId: %s' % avId)
                return
            elif obj.__class__ == self.GameAvatarClass:
                str += '%s %s\n' % (obj.accountName, obj.name)
        if not str:
            str = "No avatars."

        senderId = self.air.getAvatarIdFromSender()
        self.down_setMagicWordResponse(senderId, str)

class FakeAv:
    # fake avatar object that we can pass in to prevent magic words from crashing
    def __init__(self, senderId):
        self.hp = 100
        self.doId = senderId
        self.name = 'FakeAv'
    def b_setHp(*args):
        pass
    def b_setMojo(*args):
        pass
    def toonUp(*args):
        pass

def magicWord(mw, av=None, zoneId=0, senderId=0):
    if av is None:
        av = FakeAv(senderId)
    simbase.air.magicWordManager.doMagicWord(mw, av, zoneId, senderId)

import builtins
builtins.magicWord = magicWord
