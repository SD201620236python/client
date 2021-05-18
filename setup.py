from setuptools import setup

setup(
    name='client_docker',
    version = '0.0.1',
    author = 'Saionara',
    description = '',
    license= 'GNU',
    install_requires ='flask',
    entry_points = {
        'console_script':[
            'cli_docker = main:main'
        ]
    }
)

