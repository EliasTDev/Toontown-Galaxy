from . import Entity, BasicEntities
from pandac.PandaModules import NodePath
from direct.directnotify import DirectNotifyGlobal


class LocatorEntity(Entity.Entity, NodePath):
    notify = DirectNotifyGlobal.directNotify.newCategory('LocatorEntity')

    def __init__(self, level, entId):
        node = hidden.attachNewNode(f'LocatorEntity-{entId}')
        NodePath.__init__(self, node)
        Entity.Entity.__init__(self, level, entId)
        self.doReparent()

    def destroy(self):
        Entity.Entity.destroy(self)
        self.removeNode()

    def getNodePath(self):
        # this allows other entities to be parented to us
        return self

    def doReparent(self):
        if self.searchPath != '':
            parent = self.level.geom.find(self.searchPath)
            if parent.isEmpty():
                LocatorEntity.notify.warning(
                    f"could not find '{self.searchPath}'")
                self.reparentTo(hidden)
            else:
                self.reparentTo(parent)

    if __dev__:
        def attribChanged(self, attrib, value):
            self.doReparent()
