#!/usr/bin/env python

from typing import Dict, Iterable, List, Optional, TextIO
import cmd2
import subprocess
import colorama
import settings
from cmd2.command_definition import CommandSet


class Shell(cmd2.Cmd):

    prompt = f"{colorama.Fore.BLUE}{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}@{colorama.Fore.GREEN}{subprocess.run('hostname', shell=True, capture_output=True, text=True).stdout.strip()}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.BLUE}~{colorama.Style.RESET_ALL}$ "

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
        if settings.s['venv_manager'] == 'poetry':
            pass  # subprocess.run(['poetry shell', arg], shell=True)
        else:
            pass  # subprocess.run(arg, shell=True)
        pass

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

    def do_exit(self, arg):
        return True


if __name__ == '__main__':
    cli = Shell()
    cli.cmdloop()
