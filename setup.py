from setuptools import setup, find_packages

setup(
    name='pdp7_pt',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['django'],
    extras_require={
        'dev': ['ipdb', 'ipython'],
    },
)
