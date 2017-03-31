from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name="scoria",
    version="1.0",
    author="Jacob Durrant",
    author_email="durrantj@gmail.com",
    description="A lightweight molecule manipulation codebase.",
    url="https://git.durrantlab.com/jdurrant/scoria",
    download_url="https://git.durrantlab.com/jdurrant/scoria/repository/archive.tar.gz",
    install_requires=["numpy", "scipy"],
    packages=find_packages(),
    package_data={'scoria':['sample-files/*.pdb',
                            'sample-files/*.psf',
                            'sample-files/*.dcd',
                            'sample-files/*.pdbqt',
                            'sample-files/file_io_test.pym/*']},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research"
    ],
)
