from pandac.PandaModules import *
from direct.particles import ParticleEffect
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import AppRunnerGlobal
import os


class Drift(NodePath):
    def __init__(self, parent, renderParent):
        # Initialize the superclass
        NodePath.__init__(self)

        notify = DirectNotifyGlobal.directNotify.newCategory('DriftParticles')

        self.renderParent = renderParent.attachNewNode("driftRenderParent")
        self.renderParent.setBin("fixed", 0)
        self.renderParent.setDepthWrite(0)
        self.assign(parent.attachNewNode('drift'))
        self.effect = ParticleEffect.ParticleEffect()

        particleSearchPath = DSearchPath()
        if not __dev__:
            particleSearchPath.appendDirectory(Filename('phase_6/etc'))
        else:
            # In other environments, including the dev environment, look here:
            basePath = os.path.expandvars('$TOONTOWN') or './toontown'
            particleSearchPath.appendDirectory(
                Filename.fromOsSpecific(
                    basePath + '/src/effects'))
            particleSearchPath.appendDirectory(
                Filename('resources/phase_6/etc'))

            particleSearchPath.appendDirectory(Filename('.'))
        pfile = Filename('drift.ptf')
        found = vfs.resolveFilename(pfile, particleSearchPath)

        if not found:
            notify.warning(f'loadParticleFile() - no path: {pfile}')
            return
        notify.debug(f'Loading particle file: {pfile}')

        self.effect.loadConfig(pfile)
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_6/models/karting/driftSmoke', '**/*')

    def start(self):
        self.effect.start(self, self.renderParent)

    def stop(self):
        self.effect.disable()

    def destroy(self):
        self.stop()
        self.effect.cleanup()
        self.renderParent.removeNode()
        del self.effect
        del self.renderParent
