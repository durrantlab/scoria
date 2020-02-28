# Copyright 2017 Jacob D. Durrant
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from setuptools import setup, find_packages

setup(
    name="scoria",
    version="1.0.4",
    author="Jacob Durrant",
    author_email="durrantj@pitt.edu",
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
