# Scoria MDA is a program for manipulating 3D molecular models
# that includes MDAnalysis support.
#
# Copyright (C) 2017  Jacob D. Durrant
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Note that this version of Scoria (with MDAnalysis integration) is
# derived from the original Scoria source code, which retains its
# Apache 2.0 license.

from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name="scoria_mda",
    version="1.0.0",
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
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Intended Audience :: Science/Research"
    ],
)
