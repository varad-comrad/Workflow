#!/usr/bin/env python

import argparse, subprocess, pathlib, logging, json, sys

class CPlusPlusProj:
    def __init__(self, parsed_args: argparse.Namespace):
        self.args = parsed_args
        self.__cmds: list[str] = []
        self.__generator = self.__generator_selector()

    def __forge_generation(self):
        self.__cmds.append('forge new ' + self.args.name + self.args.lib)

    def __cmake_generation(self):
        self.__cmds.append('touch CMakeLists.txt')
        self.__cmds.append('mkdir src')
        self.__cmds.append('touch src/main.cpp')

    def __conan_generation(self):
        self.__cmds.append('conan new ' + self.args.name + '/0.1 -t')

    def __generator_selector(self):
        if self.args.manager == 'forge':
            return self.__forge_generation
        elif self.args.manager == 'cmake':
            return self.__cmake_generation
        elif self.args.manager == 'conan':
            return self.__conan_generation
        
    def generate(self):
        return subprocess.run(self.__cmds, shell=True, capture_output=True, cwd=self.args.dir).stdout.decode('utf-8').strip()
        

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', type=str)
    parser.add_argument('-d', '--dir', type=str, default='.')
    parser.add_argument('--lib', type=str, default='', action='store_const', const=' --lib')
    parser.add_argument('-m', '--manager', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = arg_parser()
    cpp_proj = CPlusPlusProj(args)
    cpp_proj.generate()