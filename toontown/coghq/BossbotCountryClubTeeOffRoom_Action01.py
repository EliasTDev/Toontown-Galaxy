from toontown.coghq.SpecImports import *

GlobalEntities = {
    # LEVELMGR
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_12/models/bossbotHQ/BossbotTeeOffRoom',
        'wantDoors': 1,
    },  # end entity 1000
    # EDITMGR
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None,
    },  # end entity 1001
    # ZONE
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [],
    },  # end entity 0
    # DOOR
    110100: {
        'type': 'door',
        'name': 'TeeOffExitDoor',
        'comment': '',
        'parentEntId': 110001,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'color': Vec4(1, 1, 1, 1),
        'isLock0Unlocked': 1,
        'isLock1Unlocked': 0,
        'isLock2Unlocked': 1,
        'isLock3Unlocked': 1,
        'isOpen': 0,
        'isOpenEvent': 0,
        'isVisBlocker': 0,
        'secondsOpen': 1,
        'unlock0Event': 0,
        'unlock1Event': 110102,
        'unlock2Event': 0,
        'unlock3Event': 0,
    },  # end entity 110100
    # MOLEFIELD
    110102: {
        'type': 'moleField',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-38.6164, -26.2922, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'numSquaresX': 6,
        'numSquaresY': 6,
        'spacingX': 10.0,
        'spacingY': 10.0,
        'timeToPlay': 60,
        'molesBase': 4,
        'molesPerPlayer': 2,
    },  # end entity 110102
    # NODEPATH
    10002: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10002
    110001: {
        'type': 'nodepath',
        'name': 'doorParent',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(60.2682, 0.55914, 0),
        'hpr': Vec3(270, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 110001
}

Scenario0 = {
}

levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0,
    ],
}
