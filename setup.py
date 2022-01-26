from setuptools import setup

setup(
    name='Toontown: Event Horizon',
    options = {
        'build_apps': {
            'console_apps': {
        #'launcher': 'start_ui_launcher.py',
        'EventHorizon': 'EventHorizon.py',
    },
    'gui_apps': {

        
    },
    'include_modules' : {
        'toontown', 'otp', 'toontown.hood'

    },
    'icons': {
        'Toontown: Event Horizon': ['galaxy_logo.jpg'],
    },
    'plugins': [
        'pandagl',
        'p3openal_audio',
        'p3tinydisplay',
        'p3fmod_audio'

    ],
            'include_patterns': [
                'Qt5Core.dll',
                'Qt5Gui.dll',
                'zoneinfo/**',
                '*.cur',
                '*.ico',
            ],
    'platforms': [
        'win_amd64',
    ]
        }
    }
    
)
