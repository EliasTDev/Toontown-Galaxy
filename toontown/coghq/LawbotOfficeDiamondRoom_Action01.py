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
        'modelFilename': 'phase_11/models/lawbotHQ/LB_Zone13a',
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
    10074: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10000,
        'attribName': 'velocity',
        'recursive': 1,
        'typeName': 'goon',
        'value': '10.0',
    },  # end entity 10074
    # GOON
    10005: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0,
    },  # end entity 10005
    10011: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0,
    },  # end entity 10011
    10017: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0,
    },  # end entity 10017
    10022: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 3.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'sg',
        'gridId': None,
        'hFov': 70,
        'strength': 15,
        'velocity': 10.0,
    },  # end entity 10022
    # MODEL
    10037: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(270, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10037
    10039: {
        'type': 'model',
        'name': 'jumpCabinet',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 1.75, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10039
    10040: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10037,
        'pos': Point3(0, 0, 4),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10040
    10041: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10057,
        'pos': Point3(0, 3.5, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10041
    10042: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10041,
        'pos': Point3(0, 0, 4),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10042
    10043: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(1.95, -4, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10043
    10044: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10051,
        'pos': Point3(1.95, 7, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10044
    10045: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -7.8, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10045
    10046: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -9.6, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10046
    10047: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -11.4, 0),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10047
    10048: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -7.8, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabB.bam',
    },  # end entity 10048
    10049: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -9.6, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabA.bam',
    },  # end entity 10049
    10050: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10054,
        'pos': Point3(0, -11.4, 4),
        'hpr': Point3(270, 0, 0),
        'scale': 1,
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_filing_cabB.bam',
    },  # end entity 10050
    10056: {
        'type': 'model',
        'name': 'stepCrate',
        'comment': '',
        'parentEntId': 10053,
        'pos': Point3(-2.08696, 1.52947, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(0.4, 0.4, 0.4),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_metal_crate.bam',
    },  # end entity 10056
    10059: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-65.7043, 26.7723, 0),
        'hpr': Vec3(30.2564, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10059
    10060: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-22.3997, 48.3291, 0),
        'hpr': Vec3(30.2564, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10060
    10061: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10062,
        'pos': Point3(-30.0586, 11.8711, 0),
        'hpr': Vec3(30.2564, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10061
    10066: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-35.5539, -11.1795, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam',
    },  # end entity 10066
    10067: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-68.8196, -28.185, 0),
        'hpr': Vec3(329.74, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10067
    10068: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-12.0298, -56.6682, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam',
    },  # end entity 10068
    10069: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(37.402, -43.7359, 0),
        'hpr': Vec3(33.69, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam',
    },  # end entity 10069
    10070: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(23.2824, -14.8496, 0),
        'hpr': Vec3(28.6105, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3.bam',
    },  # end entity 10070
    10071: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(23.28, 14.85, 0),
        'hpr': Point3(-28.61, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks3.bam',
    },  # end entity 10071
    10072: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(19.9879, 48.3291, 0),
        'hpr': Point3(-30.26, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10072
    10073: {
        'type': 'model',
        'name': 'copy of <unnamed> (3)',
        'comment': '',
        'parentEntId': 10064,
        'pos': Point3(66.6957, 25.7694, 0),
        'hpr': Vec3(333.435, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10073
    10075: {
        'type': 'model',
        'name': 'copy of <unnamed> (2)',
        'comment': '',
        'parentEntId': 10063,
        'pos': Point3(-7.27334, -24.2132, 0),
        'hpr': Vec3(326.31, 0, 0),
        'scale': Vec3(1, 1, 1),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_paper_big_stacks2.bam',
    },  # end entity 10075
    10076: {
        'type': 'model',
        'name': 'copy of <unnamed> (4)',
        'comment': '',
        'parentEntId': 10065,
        'pos': Point3(66.6957, -29.1363, 0),
        'hpr': Vec3(26.57, 0, 0),
        'scale': Vec3(2, 2, 2),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_11/models/lawbotHQ/LB_CardBoardBox.bam',
    },  # end entity 10076
    # NODEPATH
    10000: {
        'type': 'nodepath',
        'name': 'goons',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10000
    10002: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-74.9317, -1.26934, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 10002
    10003: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, -40.588, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 10003
    10004: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-44.8133, -38.3892, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
    },  # end entity 10004
    10007: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(0, 30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10007
    10008: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-10, 40, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10008
    10009: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-50, 10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10009
    10010: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10006,
        'pos': Point3(-40, 30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10010
    10013: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(15, -30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10013
    10014: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(20, -45, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10014
    10015: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(40, -15, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10015
    10016: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(55, -30, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10016
    10019: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(20, 35, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10019
    10020: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(65, -10, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10020
    10021: {
        'type': 'nodepath',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10018,
        'pos': Point3(55, 25, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10021
    10023: {
        'type': 'nodepath',
        'name': 'front',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-110, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10023
    10038: {
        'type': 'nodepath',
        'name': 'filingCabinetWall',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0, 1, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(2, 2, 2),
    },  # end entity 10038
    10051: {
        'type': 'nodepath',
        'name': 'leftCrate',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10051
    10052: {
        'type': 'nodepath',
        'name': 'rightCrate',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10052
    10053: {
        'type': 'nodepath',
        'name': 'leftCabinets',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10053
    10054: {
        'type': 'nodepath',
        'name': 'rightCabinets',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10054
    10057: {
        'type': 'nodepath',
        'name': 'cabinets',
        'comment': '',
        'parentEntId': 10053,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Point3(1, 1, 1),
    },  # end entity 10057
    10058: {
        'type': 'nodepath',
        'name': 'obstacles',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10058
    10062: {
        'type': 'nodepath',
        'name': 'leftFront',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10062
    10063: {
        'type': 'nodepath',
        'name': 'rightFront',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10063
    10064: {
        'type': 'nodepath',
        'name': 'backLeft',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10064
    10065: {
        'type': 'nodepath',
        'name': 'backRight',
        'comment': '',
        'parentEntId': 10058,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
    },  # end entity 10065
    # PATHMASTER
    10001: {
        'type': 'pathMaster',
        'name': 'rightFrontGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10002,
        'pathTarget1': 10003,
        'pathTarget2': 10004,
        'pathTarget3': 0,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0,
    },  # end entity 10001
    10006: {
        'type': 'pathMaster',
        'name': 'leftFrontGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10007,
        'pathTarget1': 10008,
        'pathTarget2': 10009,
        'pathTarget3': 10010,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0,
    },  # end entity 10006
    10012: {
        'type': 'pathMaster',
        'name': 'rightRearGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10013,
        'pathTarget1': 10014,
        'pathTarget2': 10015,
        'pathTarget3': 10016,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0,
    },  # end entity 10012
    10018: {
        'type': 'pathMaster',
        'name': 'leftRearGoon',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0,
        'pathTarget0': 10019,
        'pathTarget1': 10020,
        'pathTarget2': 10021,
        'pathTarget3': 0,
        'pathTarget4': 0,
        'pathTarget5': 0,
        'pathTarget6': 0,
        'pathTarget7': 0,
    },  # end entity 10018
}

Scenario0 = {
}

levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0,
    ],
}
