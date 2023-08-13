#!/usr/bin/env python

import cmd2, subprocess, colorama, settings

class Shell(cmd2.Cmd):
    
    prompt = f"{colorama.Fore.BLUE}{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}@{colorama.Fore.GREEN}{subprocess.run('hostname', shell=True, capture_output=True, text=True).stdout.strip()}{colorama.Fore.LIGHTBLUE_EX}:{colorama.Fore.BLUE}~{colorama.Style.RESET_ALL}$ "

    def do_run(self, arg):
        if settings.s['venv_manager'] == 'poetry':
            pass # subprocess.run(['poetry shell', arg], shell=True)
        else:
            pass # subprocess.run(arg, shell=True)
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