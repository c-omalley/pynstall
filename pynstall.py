#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# File: pynstall.py
# 
# Install python scripts and module to their respective folder as named by 
# $PYSCRIPTS or $PYMODULES
#-----------------------------------------------------------------------------

help = '''
Usage: pyinstall [-m] <script or module name(s)>

Options:

    -h  show this help message and exit
    
    -m  treat the file(s) as module(s)
'''

import os
import sys
from glob import glob
from pathlib import Path


# export PYSCRIPTS="$HOME/Projects/Scripts"
# export PYMODULES="$HOME/Projects/Modules
try:
    script_folder = Path(os.environ['PYSCRIPTS'])
    module_folder = Path(os.environ['PYMODULES'])
except KeyError:
    msg = '''Please set the environment variables PYSCRIPTS and PYMODULES.

  - Modules will be placed in the folder indicated by PYMODULES
  
  - Scripts will be placed in the folder indicated by PYMODULES
'''
    sys.exit(msg)

# Create a symbolic link to the module.
# The link will be placed in the designated folder: $PYMODULES
def _install_module(name):
    source = Path(name)
    destination = module_folder / source
    destination.symlink_to(source.resolve())


# Create a symbolic link to the script.
# The link will be placed in the designated folder: $PYSCRIPTS
def _install_script(name):
    source = Path(name)
    if 'linux' in self.platform:
        source.chmod(0o755)
        destination = script_folder /  source.stem
    else:
        destination = script_folder / source
    destination.symlink_to(source.resolve())


# Install (symlink) of a script or module into the respective folder
# designated by $PYSCRIPTS or $PYMODULES
def pynstall(name, module=False):
    if module:
        _install_module(name)
    else:
        _install_script(name)


# Run install script
if __name__ == '__main__':

    # Script arguments ("-m" flag and file list)
    arguments = sys.argv[1:]

    # Command line flag processing
    def flag(f):
        try:
            arguments.remove(f)
            return True
        except ValueError:
            return False

    # Help message?
    if flag('-h'):
        sys.exit(help)
        
    # Installing a module?
    module = flag('-m')

    # Get file list
    files = arguments
    if not files:
        # Get script(s) from the current directory
        files = glob('*.py')

    # Process files
    for filename in files:
        pynstall(filename, module)
        folder = module_folder if module else script_folder
        print(f'Installed {filename} in {folder}')

