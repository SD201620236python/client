from setuptools import setup
from setuptools.dist import check_entry_points

setup(
    name='client',
    version = '0.0.1',
    author = "Saionara",
    description = '',
    license= 'GNU',
    install_requires ='flask',
    check_entry_points = {
        'console_script':[
            'client = main:main'
        ]
    }
)