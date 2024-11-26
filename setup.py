# setup.py
from setuptools import setup, find_packages

setup(
    name='wc',
    version='0.1',
    packages=find_packages(),
    description='A Python project to count words, lines, characters, and bytes in a file',
    author='Abdul Samad',
    author_email='abdulmzsamad@gmail.com',
    entry_points={
        'console_scripts': [
            'wc=wc.wc:main',
        ],
    },
)
