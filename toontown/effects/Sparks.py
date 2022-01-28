from pandac.PandaModules import *
from direct.particles import ParticleEffect
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
import os


class Sparks(NodePath):
    def __init__(self, parent, renderParent):
        # Initialize the superclass
        NodePath.__init__(self)

        notify = DirectNotifyGlobal.directNotify.newCategory('SparkParticles')

        self.renderParent = renderParent.attachNewNode("sparkRenderParent")
        self.renderParent.setBin("fixed", 0)
        self.renderParent.setDepthWrite(0)
        self.assign(parent.attachNewNode('sparks'))
        self.effect = ParticleEffect.ParticleEffect('Sparks')

        particleSearchPath = DSearchPath()
        if not __dev__:
            particleSearchPath.appendDirectory(Filename('phase_3.5/etc'))
            particleSearchPath.appendDirectory(Filename('phase_4/etc'))
            particleSearchPath.appendDirectory(Filename('phase_5/etc'))
            particleSearchPath.appendDirectory(Filename('phase_6/etc'))
            particleSearchPath.appendDirectory(Filename('phase_7/etc'))
            particleSearchPath.appendDirectory(Filename('phase_8/etc'))
            particleSearchPath.appendDirectory(Filename('phase_9/etc'))
        else:
            # In other environments, including the dev environment, look here:
            basePath = os.path.expandvars('$TOONTOWN') or './toontown'
            particleSearchPath.appendDirectory(
                Filename.fromOsSpecific(
                    basePath + '/src/effects'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_3.5/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_4/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_5/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_6/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_7/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_8/etc'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_9/etc'))
            particleSearchPath.appendDirectory(Filename('.'))
        pfile = Filename('sparks.ptf')
        found = vfs.resolveFilename(pfile, particleSearchPath)

        if not found:
            notify.warning(f'loadParticleFile() - no path: {pfile}')
            return
        notify.debug(f'Loading particle file: {pfile}')

        self.effect.loadConfig(pfile)
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_6/models/karting/particleSpark', '**/*')

    def start(self):
        self.effect.start(self, self.renderParent)

    def stop(self):
        try:
            self.effect.disable()
        except AttributeError:
            pass

    def destroy(self):
        self.stop()
        self.effect.cleanup()
        self.renderParent.removeNode()
        del self.effect
        del self.renderParent
