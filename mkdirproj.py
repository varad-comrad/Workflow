#!/usr/bin/env python

from typing import Any
import argparse
import subprocess
import pathlib
import shutil
import settings
import errors


# def deactivate_conda_environment():
#     # Deactivate the current conda environment
#     deactivate_command = "conda deactivate"
#     subprocess.run(deactivate_command, shell=True)

class Project:
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
            if input("Project with that name already exists. Do you wish to open it(Y/N) ").lower() != "y":
                return None
        if self.args.git:
            self.__initialize_git(dirpath_aux)
        return dirpath_aux
    
    def vscode_proj(self):
        if (dir := self.__project_dir()) is None:
            return
        subprocess.run(f'code .', shell=True, cwd=dir)

    # def jupyter_proj(self, env_name: str):
    #     dir = self.__project_dir()
    #     try:
    #         # run is not working. Cannot activate conda env, shell is not recognized by conda
              # conda_name = self.args.env_name
    #         subprocess.run(f'conda init zsh && conda activate {env_name} && jupyter notebook', shell=True,
    #                                 cwd=dir)
        # except AttributeError:
            # print("ERROR: Conda environment not specified")
            # return 
        # except KeyboardInterrupt:
        #     exit_jupyter_proj()

    # def exit_jupyter_proj():
    #    process_command = "jupyter notebook list"
    #    process_output = subprocess.check_output(
    #        process_command, shell=True, text=True)
    #    process_lines = process_output.strip().split("\n")
    #    if len(process_lines) <= 1:
    #        return
    #    process_info = process_lines[1].split()
    #    pid = process_info[0]
    #    subprocess.run(f"kill {pid}", shell=True)

    # development needed
    def vim_project(self):
        pass

    def __initialize_git(self, path: pathlib.Path):
        subprocess.run('git init', shell=True, cwd=path)


# add choices to text-editor arg
def parse_project():
    text_editors = ['vscode', 'vim', 'jupyter']
    parser = argparse.ArgumentParser(usage=errors.newproj_error())
    parser.add_argument('-n', '--name',required=True, type=str)
    parser.add_argument('-t', '--text-editor',required=True, choices=text_editors)
    parser.add_argument('-d', '--dir', type=str, default=settings.default_dir)
    parser.add_argument('--new-proj', default=False, action="store_true")
    parser.add_argument('-g','--git', default=False, action="store_true")
    return parser

def main():
    proj = Project(parse_project().parse_args())
    if proj.args.text_editor == 'vscode':
        proj.vscode_proj()
    

if __name__ == '__main__':
    main()