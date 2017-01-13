#!/bin/bash

conda config --add channels MDAnalysis
conda create --name scoria numpy scipy mdanalysis

source activate scoria