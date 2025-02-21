from setuptools import find_packages
from setuptools import setup

setup(
    name='sauvc_sim',
    version='1.0.0',
    packages=find_packages(
        include=('sauvc_sim', 'sauvc_sim.*')),
)
