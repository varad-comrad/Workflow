#!/usr/bin/env python

import argparse, pathlib, subprocess, settings

def create_bash_function(filepath: pathlib.Path, name: str):
    with filepath.open('r') as f:
        with open(f"{settings.s['home_dir']}/scripts.sh", 'a') as script:
            script.write("function {}() {{\n".format(name))
            script.write('\n'.join(f.readlines()))
            script.write("\n}\n")
    filepath.unlink()

def open_text_editor(filepath: pathlib.Path):
    filepath.touch()
    subprocess.run(f'vim {filepath.absolute()}', shell=True)
    return filepath

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', type=str)
    return parser.parse_args()

def main():
    filepath = pathlib.Path(f'{settings.s["home_dir"]}/temp.sh')
    name = arg_parser().args
    open_text_editor(filepath)
    create_bash_function(filepath, name)

if __name__ == '__main__':
    main()