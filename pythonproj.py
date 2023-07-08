#!/usr/env/bin python
import argparse, subprocess
from mkdirproj import *

def wrap_parser(parser: argparse.ArgumentParser):
    parser.add_argument('--python-version', type=str, required=True) # requires poetry or pyenv to manage python versions
    parser.add_argument('--force-install', default=False, action='store_true') # force installation of python version if not present.
                                                                               # like previous, requires pyenv or poetry.
                                                                               # distinction made in settings.py
    parser.add_argument('-e', '--environment', nargs=1, type=str) # path to env. 
    parser.add_argument('-s','--set-new-env', default=False) # if user wishes to set new environment