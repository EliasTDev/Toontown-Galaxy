from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'modelFilename': 'phase_10/models/cogHQ/EndVault.bam'},
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
    0: {
        'type': 'zone',
                'name': 'UberZone',
                'comment': '',
                'parentEntId': 0,
                'scale': 1,
                'description': '',
                'visibility': []},
    10001: {
        'type': 'cogdoCraneCogSettings',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'CogFlyAwayDuration': 4.0,
        'CogFlyAwayHeight': 50.0,
        'CogMachineInteractDuration': 2.0,
        'CogSpawnPeriod': 10.0,
        'CogWalkSpeed': 12.07161265369133},
    10000: {
        'type': 'cogdoCraneGameSettings',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'EmptyFrictionCoef': 0.1,
        'GameDuration': 180.0,
        'Gravity': -32,
        'MagnetMass': 1.0,
        'MoneyBagGrabHeight': -4.1,
        'RopeLinkMass': 1.0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
             'scenarios': [Scenario0]}
