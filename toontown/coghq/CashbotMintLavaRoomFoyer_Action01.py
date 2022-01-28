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
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE18a',
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
    # ATTRIBMODIFIER
    10000: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'attribName': 'modelPath',
        'recursive': 1,
        'typeName': 'model',
        'value': '',
    },  # end entity 10000
    10001: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'attribName': 'scale',
        'recursive': 1,
        'typeName': 'model',
        'value': 'Vec3(.955,1,1)',
    },  # end entity 10001
    10019: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10015,
        'attribName': 'modelPath',
        'recursive': 1,
        'typeName': 'model',
        'value': '',
    },  # end entity 10019
    # GEAR
    10006: {
        'type': 'gear',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'degreesPerSec': -4.0,
        'gearScale': 14.193780914463838,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0,
    },  # end entity 10006
    10007: {
        'type': 'gear',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 4.28999996185),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'degreesPerSec': 4.0,
        'gearScale': 14.193780914463838,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0,
    },  # end entity 10007
    10009: {
        'type': 'gear',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 8.57999992371),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'degreesPerSec': -4.0,
        'gearScale': 14.193780914463838,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0.055,
    },  # end entity 10009
    10014: {
        'type': 'gear',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 12.8699998856),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'degreesPerSec': 4.0,
        'gearScale': 14.193780914463838,
        'modelType': 'mint',
        'orientation': 'horizontal',
        'phaseShift': 0.059999999999999998,
    },  # end entity 10014
    # HEALBARREL
    10018: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10017,
        'pos': Point3(-2.03643107414, 2.34967470169, 5.46433734894),
        'hpr': Vec3(34.1522636414, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 5,
        'rewardPerGrabMax': 0,
    },  # end entity 10018
    # MODEL
    10002: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(6.5, 6.5, 6.5),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/RoundShadow.bam',
    },  # end entity 10002
    10005: {
        'type': 'model',
        'name': 'doorwayCrate',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(27.0090961456, 0.850000023842, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10005
    10008: {
        'type': 'model',
        'name': 'shaft',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 7.25891637802),
        'hpr': Vec3(0.0, 0.0, 180.0),
        'scale': Vec3(5.35842609406, 5.35842609406, 5.35842609406),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModel',
        'modelPath': 'phase_10/models/cashbotHQ/MintGearPost.bam',
    },  # end entity 10008
    10010: {
        'type': 'model',
        'name': 'middle',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.954999983311, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10010
    10011: {
        'type': 'model',
        'name': 'copy of middle',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(-5.72357320786, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.954999983311, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10011
    10012: {
        'type': 'model',
        'name': 'copy of middle',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(5.71999979019, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.954999983311, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10012
    10013: {
        'type': 'model',
        'name': 'copy of middle',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(11.4399995804, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(0.954999983311, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10013
    10015: {
        'type': 'model',
        'name': 'crateStack',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-18.0376968384, 20.2023410797, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10015
    10016: {
        'type': 'model',
        'name': 'upper',
        'comment': '',
        'parentEntId': 10015,
        'pos': Point3(0.0, 0.0, 5.42841148376),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10016
    10017: {
        'type': 'model',
        'name': 'copy of upper',
        'comment': '',
        'parentEntId': 10016,
        'pos': Point3(0.0, 0.0, 5.43412637711),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cogHQ/CBMetalCrate2.bam',
    },  # end entity 10017
    10021: {
        'type': 'model',
        'name': 'crateStack',
        'comment': '',
        'parentEntId': 10020,
        'pos': Point3(21.064825058, 20.1899757385, 9.87216758728),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam',
    },  # end entity 10021
    # NODEPATH
    10003: {
        'type': 'nodepath',
        'name': 'gears',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-3.18650078773, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
    },  # end entity 10003
    10004: {
        'type': 'nodepath',
        'name': 'wall',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(19.5468139648, 6.37875938416, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.95812249184, 1.5, 1.79999995232),
    },  # end entity 10004
    10020: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
    },  # end entity 10020
}

Scenario0 = {
}

levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0,
    ],
}
