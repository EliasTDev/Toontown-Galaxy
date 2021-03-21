from setuptools import setup

setup(
    name='Toontown Galaxy',
    options = {
        'build_apps': {
            'console_apps': {
        'Toontown Galaxy': 'main.py',
    },
    'plugins': [
        'pandagl',
        'p3openal_audio',
        'p3tinydisplay'
        'pandadx9'

    ],
            'include_patterns': [
                'resources/BuiltFiles/*.mf',
            ],
    'platforms': [
        'win_amd64',
    ]
        }
    }
    
)