#!/bin/bash

conda config --add channels MDAnalysis
conda create --name pymolecule numpy scipy mdanalysis

source activate pymolecule