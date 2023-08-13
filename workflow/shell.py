#!/usr/bin/env python

from typing import Dict, Iterable, List, Optional, TextIO
import cmd2, os, subprocess, colorama, settings, pathlib
from cmd2.command_definition import CommandSet


def get_shortened_path(path):
    home = os.path.expanduser("~")
    if path.startswith(home):
        rel_path = os.path.relpath(path, home)
        return f"~/{rel_path}" if rel_path else "~"
    return path

class Shell(cmd2.Cmd):

    path = pathlib.Path('.')
    prompt = f"{colorama.Fore.GREEN}{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}@{colorama.Fore.GREEN}{subprocess.run('hostname', shell=True, capture_output=True, text=True).stdout.strip()}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.CYAN}{get_shortened_path(path.absolute().as_posix())}{colorama.Style.RESET_ALL}$ "

    # highlighted_keywords = ['exit', 'mkdb', 'config', 'mkdir',
    #                         'pyproj', 'new', 'push', 'bash', 'clear', 'git']
    # colors = {
    #     'exit': colorama.Fore.CYAN,
    #     'mkdb': colorama.Fore.CYAN,
    #     'config': colorama.Fore.CYAN,
    #     'mkdir': colorama.Fore.CYAN,
    #     'pyproj': colorama.Fore.CYAN,
    #     'new': colorama.Fore.CYAN,
    #     'push': colorama.Fore.CYAN,
    #     'bash': colorama.Fore.CYAN,
    #     'clear': colorama.Fore.CYAN,
    #     'git': colorama.Fore.CYAN
    # }

    # def precmd(self, statement):
    #     # Apply syntax highlighting to the command if it's a keyword
    #     if statement.command in self.highlighted_keywords:
    #         statement.command = self.colorize(
    #             statement.command, color=colorama.Fore.CYAN)
    #     return statement

    def do_run(self, arg):
        path = pathlib.Path('.')
        lang = ''
        aux = path
        for element in path.iterdir():
            if element.is_dir():
                if (element / '__main__.py').exists():
                    aux = element
                    lang = 'python'
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                elif (element / 'main.rs').exists():
                    aux = element
                    lang = 'rust'
        if lang == 'python' and settings.s['venv_manager'] != 'poetry':
            ret = subprocess.run(
                f'python {aux.absolute()}', shell=True, capture_output=True, text=True).stdout.strip()
        elif lang == 'python' and settings.s['venv_manager'] == 'poetry':
            pass  # subprocess.run(['poetry shell', arg], shell=True)
        else:
            ret = subprocess.run(
                arg, shell=True, capture_output=True, text=True).stdout.strip()
        print(ret)

    def do_config(self, arg):
        subprocess.run('config.py ' + arg, shell=True)

    def do_mkdir(self, arg):
        subprocess.run('mkdirproj.py ' + arg, shell=True)

    def do_pyproj(self, arg):
        subprocess.run('pyproj.py ' + arg, shell=True)

    def do_new(self, arg):
        subprocess.run('make_workflow.py ' + arg, shell=True)

    def do_mkdb(self, arg):
        subprocess.run('mkdb.py ' + arg, shell=True)

    def do_push(self, arg):
        subprocess.run('push_git.py ' + arg, shell=True)

    def do_bash(self, arg):
        subprocess.run(arg, shell=True)

    def do_clear(self, arg):
        subprocess.run('clear', shell=True)

    def do_git(self, arg):
        subprocess.run('git ' + arg, shell=True)

    def do_cd(self, arg):
        self.path /= arg
        os.chdir(arg)
        self.prompt = f"{colorama.Fore.GREEN}{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}@{colorama.Fore.GREEN}{subprocess.run('hostname', shell=True, capture_output=True, text=True).stdout.strip()}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.CYAN}{get_shortened_path(self.path.absolute().as_posix())}{colorama.Style.RESET_ALL}$ "

    def do_ls(self, arg):
        subprocess.run('ls ' + arg, shell=True)

    def do_python(self, arg):
        subprocess.run('python ' + arg, shell=True)

    def do_cargo(self, arg):
        subprocess.run('cargo ' + arg, shell=True)

    def do_make(self, arg):
        subprocess.run('make ' + arg, shell=True)

    def do_cmake(self, arg):
        subprocess.run('cmake ' + arg, shell=True)

    def do_gcc(self, arg):
        # TODO: CHECK IF arg IS C++ OR C FILE AND CALL THE CORRECT COMPILER
        subprocess.run('cmake ' + arg, shell=True)

    def do_java(self, arg):
        # TODO: A LOT ACTUALLY
        subprocess.run('cmake ' + arg, shell=True)

    def do_exit(self, arg):
        return True


if __name__ == '__main__':
    cli = Shell()
    cli.cmdloop()
