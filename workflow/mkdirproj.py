#!/usr/bin/env python

# TODO: Convert multiple text editors methods to a single one using a dictionary
from typing import Any
import argparse, subprocess, pathlib, shutil, settings, errors, sys

class Project:
    command = {
        'vscode': 'code',
        'pycharm': 'pycharm-community',
        'vim': 'vim'
    }
    def __init__(self, parser_args: argparse.Namespace)-> None:
        self.args = parser_args
        self.dirpath: pathlib.Path = pathlib.Path(self.args.dir)

    def __project_dir(self) -> None | pathlib.Path:
        dirpath_aux = self.dirpath.joinpath(self.args.name)
        if self.args.new_proj and dirpath_aux.exists():
            shutil.rmtree(dirpath_aux.absolute())
        try:
            dirpath_aux.mkdir(parents=True)
        except FileExistsError:
            if i:=input("Project with that name already exists. Do you wish to open it(Y/N) ").lower() == "y":
                return dirpath_aux
            elif i == 'n':
                return None
            else:
                raise ValueError("Unexpected result")
        
        if self.args.git_clone and self.args.new_proj:
            self.__git_clone(dirpath_aux)
            dirpath_aux = list(dirpath_aux.iterdir())[0] # check if necessary

        if self.args.git and not self.args.git_clone and self.args.new_proj:
            self.__initialize_git(dirpath_aux)
        
        self.dirpath = dirpath_aux
        return dirpath_aux
    
    def jupyter_proj(self):
        dir = self.__project_dir()
        try:
            subprocess.run(f'jupyter notebook', shell=True, cwd=dir)
        except KeyboardInterrupt:
            self.exit_jupyter_proj()

    def exit_jupyter_proj(self):
       subprocess.run('jupyter notebook stop -y', shell=True)

    def open_proj(self):
        if (dir := self.__project_dir()) is None:
            return
        subprocess.run(f'{self.command[self.args.text_editor]} .', shell=True, cwd=dir)

    def __initialize_git(self, path: pathlib.Path):
        subprocess.run('git init', shell=True, cwd=path)

    def __git_clone(self, path: pathlib.Path):
        subprocess.run(f'git clone {self.args.git_clone}', shell=True, cwd=path)
        


# add choices to text-editor arg
def parse_project():
    text_editors = ['vscode', 'vim', 'jupyter']
    parser = argparse.ArgumentParser(usage=errors.newproj_error())
    parser.add_argument('-n', '--name',required=True, type=str)
    parser.add_argument('-t', '--text-editor',required=True, choices=text_editors)
    parser.add_argument('-d', '--dir', type=str, default=settings.default_dir)
    parser.add_argument('--new-proj', default=False, action="store_true")
    parser.add_argument('-g','--git', default=False, action="store_true")
    parser.add_argument('-gc', '--git-clone', type=str, default=False)
    return parser

def main():
    proj = Project(parse_project().parse_args())
    if proj.args.text_editor == 'jupyter':
        proj.jupyter_proj()
    else:
        proj.open_proj()
    sys.exit(proj.dirpath)
    


if __name__ == '__main__':
    main()