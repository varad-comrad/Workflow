#!/usr/bin/env python
import argparse, subprocess, pathlib, settings
# from mkdirproj import *

def parse_pyproject():
    parser = argparse.ArgumentParser()
    # requires pyenv to manage python versions
    parser.add_argument('-p','--python-version', type=str, required=True)
    
    parser.add_argument('-f','--force-install', default=False, action='store_true')
    # force installation of python version if not present.
    # like previous, requires pyenv.
    
    parser.add_argument('-e', '--environment', nargs=1, type=str)
    # path to env.

    parser.add_argument('-s', '--set-new-env', nargs='+', default=False)
    # if user wishes to set new environment. If specified, argument must be the name of the venv and the path to requirements.txt
    # for pip installation. Second argument is optional. Tool for managing may be conda or poetry or virtualenv.
    # Defined in settings.py

    return parser.parse_args()

class PyProject:
    def __init__(self, parsed_args: argparse.Namespace):
        if len(parsed_args.set_new_env) > 2:
            raise ValueError('Set new environment must have at most 2 arguments') # change error type later
        self.args = parsed_args

    def __new_venv(self):
        match settings.venv_manager:
            case 'virtualenv':
                subprocess.run(f"virtualenv --python=python{self.args.python_version} '{self.args.set_new_env[0]}'", cwd='.', shell=True)
                # subprocess.run(f"source {self.args.set_new_env[0]}/bin/activate", cwd='.', shell=True)
            case 'conda':
                pass
            case 'poetry':
                pass

        path = pathlib.Path('./requirements.txt')
        if path.exists():
            self.__pip_install()

    def __pip_install(self):
        subprocess.run(f'pip install -r {self.args.set_new_env[1]}', cwd='.', shell=True)
    
    def choose_venv(self):
        self.__new_venv()

    def __install_version(self):
        subprocess.run(f'pyenv install {self.args.python_version}', shell=True, cwd='.')

    def choose_version(self):
        res = subprocess.check_output('pyenv versions', shell=True, cwd='.')
        if self.args.python_version not in res and self.args.force_install:
            self.__install_version()
        subprocess.run(f'pyenv local {self.args.python_version}', shell=True, cwd='.')


def main():
    PyProject(parse_pyproject()).choose_venv()



if __name__ == '__main__':
    main()