#!/bin/bash
#
# request Bourne shell as shell for job
#$ -S /bin/bash
#
# Your job name 
#$ -N telmain
#
# Use current working directory
#$ -cwd
#
# Join stdout and stderr
#$ -j y
#
# Currently only sld5 support
#$ -l os=sld6
#
# The following is for reporting only. It is not really needed
# to run the job. It will show up in your output file.

# Reuse prepared MPD host file

export ROOTSYS=/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/v01-17-06/root/5.34.18
export LCIO=/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/v01-17-06/lcio/v02-05
export PYTHONPATH=$ROOTSYS/lib:$LCIO/src/python:$PYTHONPATH
export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH

/usr/bin/python /nfs/dust/ilc/user/bboitrel/for-benjamin/telmain.py
