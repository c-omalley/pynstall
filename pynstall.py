#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# File: pynstall.py
# Date: 2019-06-22
#-----------------------------------------------------------------------------
# Synopsis
#-----------------------------------------------------------------------------

import os
import sys
from glob import glob
from pathlib import Path


# export SCRIPTS="$HOME/Scripts"
script_folder = Path(os.environ['SCRIPTS'])


# Create a symbolic link to the script.
# The link will be placed in the designated folder.
def pynstall(name):
    source = Path(name)
    if 'linux' in sys.platform:
        destination = script_folder / source.stem
    else:
        destination = script_folder / source
    destination.symlink_to(source.resolve())


# Copy scripts to the script folder
if __name__ == '__main__':
    files = sys.argv[1:]
    if not files:
        # Get script(s) from the current directory
        files = glob('*.py')
    for filename in files:
        pynstall(filename)
        print(f'Installed {filename} in {script_folder}')

