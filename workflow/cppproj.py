#!/usr/bin/env python

import argparse, subprocess, pathlib, logging, json, sys

class CPlusPlusProj:
    def __init__(self, parsed_args: argparse.Namespace):
        self.args = parsed_args
        self.cmds = [f'cd {self.args.dir}']

    def __forge_generation(self):
        self.cmds.append('forge new ' + self.args.name + self.args.lib)

    def __cmake_generation(self):
        pass

    def __generate_directory_tree(self):
        pass

    def __generate_project_manager_file(self):
        pass

    def __generate_main_package(self):
        pass    
    
    pass

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', type=str)
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('--lib', type=str, default='', action='store_const', const=' --lib')
    parser.add_argument('-m', '--manager', type=str)
    return parser.parse_args()
