import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements=[
   'requests',
   'bpython',
   'ipython',
   'django==1.6'
]


setup(
    name="proj",
    version="0.0.2",
    author="Andrew Carter",
    author_email="andrewjcarter@gmail.com",
    description=('pequeno projeto para testar setup.py'),
    license="BSD",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['proj', 'tests', 'proj2'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Framework :: Pytest",
        "Framework :: Setuptools Plugin"
    ],
)
