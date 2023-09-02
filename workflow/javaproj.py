#!/usr/bin/env python

import argparse, subprocess, pathlib, logging, json, sys

class JavaProj:
    def __init__(self, parsed_args: argparse.Namespace):
        self.args = parsed_args
        # self.cmds = [f'cd {self.args.dir}']

    def __generate_directory_tree(self):
        pass

    def __generate_project_manager_file(self):
        pass

    def __generate_main_package(self):
        pass    

    def __generate_test_package(self):
        pass

    
    pass

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', type=str)
    parser.add_argument('-v', '--java-version', type=str)
    parser.add_argument('-n', '--name', type=str)
    parser.add_argument('-m', '--manager', type=str)
    return parser.parse_args()
