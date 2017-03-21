from __future__ import absolute_import
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

setup(
    name="scoria",
    version="1.0",
    author="Jacob Durrant",
    author_email="durrantj@gmail.com",
    description="A lightweight molecule manipulation codebase.",
    install_requires=["numpy", "scipy", "six", "mdanalysis", "prody"],
    packages=find_packages(),
    package_data={'scoria':['sample-files/*.pdb',
                            'sample-files/*.psf',
                            'sample-files/*.dcd',
                            'sample-files/*.pdbqt',
                            'sample-files/file_io_test.pym/*']},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research",

    ],
)
