#!/usr/bin/env python

import pathlib, subprocess, settings

def run_code(path: pathlib.Path):
    if path.is_file():
        match path.name.split('.')[-1]:
            case 'py':
                subprocess.run(f'python {path.name}', shell=True)
            case 'c':
                subprocess.run(
                    f'gcc {path.name} -o {path.name.split(".")[0]} && ./{path.name.split(".")[0]}', shell=True)
            case 'cpp':
                subprocess.run(
                    f'g++ {path.name} -o {path.name.split(".")[0]} && ./{path.name.split(".")[0]}', shell=True)
            case 'rs':
                subprocess.run(f'rustc {path.name} && ./{path.name.split(".")[0]}', shell=True)
            case 'js':
                subprocess.run(f'node {path.name}', shell=True)
            case 'java':
                subprocess.run(
                    f'javac {path.name} && java {path.name.split(".")[0]}', shell=True)
            case 'go':
                pass
            case 'zig':
                pass
            
        pass
    pass
