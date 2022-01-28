from toontown.coghq.SpecImports import *
import random

GlobalEntities = {
    # LEVELMGR
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone03a',
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
    # ENTRANCEPOINT
    10000: {
        'type': 'entrancePoint',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 6, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'entranceId': 0,
        'radius': 15,
        'theta': 20,
    },  # end entity 10000
    # MODEL
    100000: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB',
    },  # end entity 100000
    100001: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100002,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 180),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB',
    },  # end entity 100001
    100004: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100003,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB',
    },  # end entity 100004
    100006: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100005,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 180),
        'scale': Point3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_torch_lampB',
    },  # end entity 100006
    100008: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100007,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1.5, 1.5, 1.5),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_twist_stacks',
    },  # end entity 100008
    100010: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100009,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(180, 0, 180),
        'scale': Point3(1.5, 1.5, 1.5),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_twist_stacks',
    },  # end entity 100010
    100012: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100011,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox',
    },  # end entity 100012
    100013: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100014,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 180),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox',
    },  # end entity 100013
    100016: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100015,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1.5, 1.5, 1.5),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_couchA',
    },  # end entity 100016
    100017: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 100018,
        'pos': Point3(0, 0, 0),
        'hpr': Point3(0, 0, 180),
        'scale': Point3(1.5, 1.5, 1.5),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_couchA',
    },  # end entity 100017
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
    10004: {
        'type': 'nodepath',
        'name': 'lamp',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-10.1845, 16.3439, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 10004
    100003: {
        'type': 'nodepath',
        'name': 'lamp2',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(10.3093, 14.7794, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 100003
    100007: {
        'type': 'nodepath',
        'name': 'paper',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(14.3907, 11.4389, 0),
        'hpr': Vec3(300.379, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 100007
    100011: {
        'type': 'nodepath',
        'name': 'box',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(-18.5313, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 100011
    100015: {
        'type': 'nodepath',
        'name': 'couch',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(14.3585, -9.43671, 0),
        'hpr': Vec3(270.699, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 100015
    # RENDERING
    100002: {
        'type': 'rendering',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'blending': 'Normal',
        'colorA': 1.0,
        'colorB': 1.0,
        'colorG': 1.0,
        'colorR': 1.0,
        'fogOn': 0,
        'renderBin': 'default',
    },  # end entity 100002
    100005: {
        'type': 'rendering',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100003,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'blending': 'Normal',
        'colorA': 1.0,
        'colorB': 1.0,
        'colorG': 1.0,
        'colorR': 1.0,
        'fogOn': 0,
        'renderBin': 'default',
    },  # end entity 100005
    100009: {
        'type': 'rendering',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100007,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'blending': 'Normal',
        'colorA': 1.0,
        'colorB': 1.0,
        'colorG': 1.0,
        'colorR': 1.0,
        'fogOn': 0,
        'renderBin': 'default',
    },  # end entity 100009
    100014: {
        'type': 'rendering',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100011,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'blending': 'Normal',
        'colorA': 1.0,
        'colorB': 1.0,
        'colorG': 1.0,
        'colorR': 1.0,
        'fogOn': 0,
        'renderBin': 'default',
    },  # end entity 100014
    100018: {
        'type': 'rendering',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 100015,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'blending': 'Normal',
        'colorA': 1.0,
        'colorB': 1.0,
        'colorG': 1.0,
        'colorR': 1.0,
        'fogOn': 0,
        'renderBin': 'default',
    },  # end entity 100018
}

Scenario0 = {
}

levelSpec = {
    'globalEntities': GlobalEntities, 'scenarios': [
        Scenario0, ], 'titleString': (
            f"MemTag: LawbotOfficeEntrance_Action00 {random.random()}")}
