#!/usr/bin/env python
import argparse, subprocess
from mkdirproj import *

def wrap_parser(parser: argparse.ArgumentParser):
    parser.add_argument('-l', '--lib', default=False, action='store_true')
    parser.add_argument('-p', '--packages', nargs='*', required=False, type=str)
    parser.add_argument('')
