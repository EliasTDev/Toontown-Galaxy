from toontown.toonbase import ToontownGlobals
from . import SellbotLegFactorySpec
from . import SellbotLegFactoryCogs
from . import LawbotLegFactorySpec
from . import LawbotLegFactoryCogs

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactorySpec,
 ToontownGlobals.LawbotOfficeInt: LawbotLegFactorySpec}
CogSpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactoryCogs,
 ToontownGlobals.LawbotOfficeInt: LawbotLegFactoryCogs}

if config.GetBool('want-brutal-factory', True):
    from . import SellbotMegaCorpLegSpec
    from . import SellbotMegaCorpLegCogs
    FactorySpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegSpec
    CogSpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegCogs
