from direct.showbase.PythonUtil import listToItem2index
from otp.namepanel.PickANamePattern import PickANamePatternTwoPartLastName
from toontown.makeatoon.NameGenerator import NameGenerator
import types


class TTPickANamePattern(PickANamePatternTwoPartLastName):
    NameParts = None
    LastNamePrefixesCapped = None

    def _getNameParts(self):
        if TTPickANamePattern.NameParts is None:
            TTPickANamePattern.NameParts = {}
            ng = NameGenerator()
            TTPickANamePattern.NameParts = ng.getNameParts()

        # make sure the dicts haven't been inverted
        #assert type(list(TTPickANamePattern.NameParts[gender][0].keys())[0]) is bytes

        return TTPickANamePattern.NameParts

    def _getLastNameCapPrefixes(self):
        if TTPickANamePattern.LastNamePrefixesCapped is None:
            ng = NameGenerator()
            TTPickANamePattern.LastNamePrefixesCapped = ng.getLastNamePrefixesCapped()[
                :]

        return TTPickANamePattern.LastNamePrefixesCapped


if not __debug__:
    assert TTPickANamePattern('Alvin').hasNamePattern()
    assert TTPickANamePattern('Fireball').hasNamePattern()
    assert TTPickANamePattern('King Alvin Sourflap').hasNamePattern()
    assert not TTPickANamePattern('King Alvin ASDFflap').hasNamePattern()
    assert not TTPickANamePattern('test name').hasNamePattern()

    assert TTPickANamePattern('').getNameString(TTPickANamePattern(
        'King Alvin Sourflap').getNamePattern()) == 'King Alvin Sourflap'
    assert TTPickANamePattern('').getNameString(TTPickANamePattern(
        'Knuckles McFlipper').getNamePattern()) == 'Knuckles McFlipper'
