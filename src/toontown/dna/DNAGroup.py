from .common import *
from . import DNAUtil

class DNAGroup:
    COMPONENT_CODE = 1

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.visGroup = None

    def add(self, child):
        self.children += [child]

    def remove(self, child):
        self.children.remove(child)

    def at(self, index):
        return self.children[index]

    def setParent(self, parent):
        self.parent = parent
        self.visGroup = parent.getVisGroup()

    def getParent(self):
        return self.parent

    def clearParent(self):
        self.parent = None
        self.visGroup = None

    def getVisGroup(self):
        return self.visGroup

    def getNumChildren(self):
        return len(self.children)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def makeFromDGI(self, dgi):
        self.name = DNAUtil.dgiExtractString8(dgi)
        DNAUtil.dgiExtractString8(dgi)
        DNAUtil.dgiExtractString8(dgi)

    def traverse(self, np, store):
        _np = np.attachNewNode(self.name)
        self.traverseChildren(_np, store)

    def traverseChildren(self, np, store):
        for child in self.children:
            child.traverse(np, store)
