#!/usr/bin/env python

import sys, subprocess, pathlib


def modify_rcs(alias, command):
    home = pathlib.Path(
        f'/home/{subprocess.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()}')
    rcs = []
    for element in home.iterdir():
        if element.name == '.zshrc':
            rcs.append(home / '.zshrc')
        if element.name == '.fishrc':
            rcs.append(home / '.fishrc')
        if element.name == '.bashrc':
            rcs.append(home / '.bashrc')
        if element == '.kshrc':
            rcs.append(home / '.kshrc')
        if element == '.cshrc':
            rcs.append(home / '.cshrc')
        if element == '.tcshrc':
            rcs.append(home / '.tcshrc')
        if element == '.dashrc':
            rcs.append(home / '.dashrc')
    for rc in rcs:
	    with rc.open('a') as file:
		    file.write(
				f'\n\n{alias_string(alias, command)}\n\n')


def alias_string(alias, command):
    return f'alias {alias}="{command}"'

def main():
    alias, command = sys.argv[1], sys.argv[2]
    modify_rcs(alias, command)

if __name__ == '__main__':
     main()
