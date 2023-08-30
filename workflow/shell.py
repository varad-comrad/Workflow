#!/usr/bin/env python

import cmd2, os, subprocess, colorama, settings, pathlib
from typing import Optional, TextIO, List, Iterable, Dict
from cmd2 import CommandSet
import re



def shortened_path(path: pathlib.Path, user: str):
    ret = path.absolute().as_posix()
    if ret.startswith(f'/home/{user}'):
       ret = ret.replace(f'/home/{user}', '~')
    if ret.endswith('..'):
        ret = ret.replace('/..', '')
    return ret


class Shell(cmd2.Cmd):

    path = pathlib.Path('.')

    user = subprocess.run('whoami', shell=True,
                          capture_output=True, text=True).stdout.strip()
    
    host = subprocess.run('hostname', shell=True,
                          capture_output=True, text=True).stdout.strip()
    
    prompt = f"{colorama.Fore.BLUE}{user}@{colorama.Fore.GREEN}{host}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.CYAN}{shortened_path(path, user)}{colorama.Style.RESET_ALL}$ "

    def __init__(self, completekey: str = 'tab',
                 stdin: Optional[TextIO] = None,
                 stdout: Optional[TextIO] = None,
                 *,
                 persistent_history_file: str = '',
                 persistent_history_length: int = 1000,
                 startup_script: str = '',
                 silence_startup_script: bool = False,
                 include_py: bool = False,
                 include_ipy: bool = False,
                 allow_cli_args: bool = True,
                 transcript_files: Optional[List[str]] = None,
                 allow_redirection: bool = True,
                 multiline_commands: Optional[List[str]] = None,
                 terminators: Optional[List[str]] = None,
                 shortcuts: Optional[Dict[str, str]] = None,
                 command_sets: Optional[Iterable[CommandSet]] = None,
                 auto_load_commands: bool = True,
                 ) -> None:
        
        super().__init__(completekey,
                       stdin,
                       stdout,
                       
                       persistent_history_file = persistent_history_file,
                       persistent_history_length = persistent_history_length,
                       startup_script = startup_script,
                       silence_startup_script = silence_startup_script,
                       include_py = include_py,
                       include_ipy = include_ipy,
                       allow_cli_args = allow_cli_args,
                       transcript_files = transcript_files,
                       allow_redirection = allow_redirection,
                       multiline_commands = multiline_commands,
                       terminators = terminators,
                       shortcuts = shortcuts,
                       command_sets = command_sets,
                       auto_load_commands = auto_load_commands,)
        subprocess.run('clear', shell=True)

    # highlighted_keywords = ['exit', 'mkdb', 'config', 'mkdir',
    #                         'pyproj', 'new', 'push', 'bash', 'clear', 'git']
    # colors = {
    #     'exit': colorama.Fore.BLUE,
    #     'mkdb': colorama.Fore.BLUE,
    #     'config': colorama.Fore.BLUE,
    #     'mkdir': colorama.Fore.BLUE,
    #     'pyproj': colorama.Fore.BLUE,
    #     'new': colorama.Fore.BLUE,
    #     'push': colorama.Fore.BLUE,
    #     'bash': colorama.Fore.BLUE,
    #     'clear': colorama.Fore.BLUE,
    #     'git': colorama.Fore.BLUE
    # }

    # def precmd(self, statement):
    #     # Apply syntax highlighting to the command if it's a keyword
    #     if statement.command in self.highlighted_keywords:
    #         color = self.colors.get(statement.command, colorama.Fore.CYAN)
    #         statement.command = f"{color}{statement.command}{colorama.Style.RESET_ALL}"
    #     return statement


    def do_run(self, arg):
        #TODO: Implement a code runner separately
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

    def do_cd(self, arg: str):
        # TODO: Debug and implement the cases where arg is '-' and '~' and '..'
        prev = self.path
        for argument in arg.split('/'):
            if argument == '..':
                self.path = self.path.absolute().parent
            elif argument == '-':
                pass
            elif argument == '~':
                self.path = pathlib.Path(*pathlib.Path(subprocess.run(
                    'pwd', shell=True, capture_output=True, text=True).stdout.strip()).absolute().parts[:3]).absolute()
            else:
                self.path /= argument
        try:
            os.chdir(self.path.absolute())
            self.prompt = f"{colorama.Fore.BLUE}{self.user}@{colorama.Fore.GREEN}{self.host}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.CYAN}{shortened_path(self.path, self.user)}{colorama.Style.RESET_ALL}$ "
        except FileNotFoundError:
            print(f'No such file or directory: {self.path}')
            self.path = prev

    def do_ls(self, arg):
        subprocess.run('ls ' + arg, shell=True)

    def do_man(self, arg):
        pass

    def do_python(self, arg):
        subprocess.run('python ' + arg, shell=True)

    def do_cargo(self, arg):
        subprocess.run('cargo ' + arg, shell=True)

    def do_make(self, arg):
        subprocess.run('make ' + arg, shell=True)

    def do_cmake(self, arg):
        subprocess.run('cmake ' + arg, shell=True)

    def do_gcc(self, arg):
        if re.findall(r'.*\.c\b', arg):
            print('gcc')
            subprocess.run('gcc ' + arg, shell=True)
        else:
            print('g++')
            subprocess.run('g++ ' + arg, shell=True)

    def do_gpp(self, arg):
        subprocess.run('g++ ' + arg, shell=True)

    def do_javac(self, arg):
        subprocess.run('javac ' + arg, shell=True)
    
    def do_java(self, arg):
        subprocess.run('java ' + arg, shell=True)
    
    def do_maven(self, arg):
        subprocess.run('maven ' + arg, shell=True)

    def do_gradle(self, arg):
        subprocess.run('gradle ' + arg, shell=True)

    def do_ant(self, arg):
        subprocess.run('ant ' + arg, shell=True)

    def do_exit(self, arg):
        subprocess.run('clear', shell=True)
        return True



if __name__ == '__main__':
    cli = Shell(shortcuts={':q': 'exit', ':g': 'git', 'g++': 'gpp'}, include_ipy=True)
    cli.cmdloop()
