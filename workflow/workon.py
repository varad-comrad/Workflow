#!/usr/bin/env python

import sys, subprocess, pathlib, settings

def venv_lookup(venv_name: str) -> bool:
    return pathlib.Path(venv_name) in pathlib.Path('.').iterdir()

def create_venv(venv_name: str) -> None:
    subprocess.run(f'virtualenv {venv_name}', shell=True, capture_output=True, text=True)

def main():
    try:
        venv_name = sys.argv[1]
        if not venv_lookup(venv_name):
            create_venv() 
        print(f'source {venv_name}/bin/activate')    
    except IndexError:
        create_venv(settings.s.get("default_name_venv", "my_venv"))
        print(
            f'source {settings.s.get("default_name_venv", "my_venv")}/bin/activate')


if __name__ == '__main__':
    main()