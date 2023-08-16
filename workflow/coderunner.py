#!/usr/bin/env python

import pathlib, subprocess, glob, sys, argparse, logging


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
            case 'ts':
                subprocess.run(f'ts-node {path.name}', shell=True)
            case 'java':
                subprocess.run(
                    f'javac {path.name} && java {path.name.split(".")[0]}', shell=True)
            case 'kt': #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                subprocess.run(
                    f'javac {path.name} && java {path.name.split(".")[0]}', shell=True)
            case 'kts':  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                subprocess.run(
                    f'javac {path.name} && java {path.name.split(".")[0]}', shell=True)
            case 'jl':
                subprocess.run(
                    f'julia {path.name}', shell=True)
            case 'csproj':
                subprocess.run(
                    f'dotnet run --project {path.name}', shell=True)
            case 'go':
                subprocess.run(
                    f'go run {path.name}', shell=True)
            case 'v':
                subprocess.run(
                    f'v run {path.name}', shell=True)
            case 'zig':
                subprocess.run(
                    f'zig run {path.name}', shell=True)
            case 'nim':
                subprocess.run(
                    f'nim compile --verbosity:0 --hints:off --run {path.name}', shell=True)
            case _:
                pass
        return     

    if any((element.endswith('__main__.py') or element.endswith('main.py')) for element in glob.iglob(path.name, recursive=True)):
        subprocess.run(f'python {path.name}', shell=True)
    elif pathlib.Path('pyproject.toml') in path.iterdir():
        subprocess.run(f'poetry {path.name}', shell=True)
    elif pathlib.Path('cargo.toml') in path.iterdir():
        subprocess.run(f'cargo run', shell=True)    
    # elif pathlib.Path('cargo.toml') in path.iterdir():
    #     subprocess.run(f'cargo run', shell=True)
    return 

def debug_code():
    pass

def test_code():
    pass

def bench_code():
    pass

def build_code():
    pass


def runner():
    path = pathlib.Path(sys.argv[1])
    ret = run_code(path)
    print('\n' * 3 + 'Code returned with exit code ' + ret)
    return ret # exit code

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', type=str, default='.')
    parser.add_argument('--build', action='store_true', default=False)
    parser.add_argument('--test', action='store_true', default=False)
    parser.add_argument('--bench', action='store_true', default=False)
    parser.add_argument('--debug', action='store_true', default=False)
    # TODO: not allow these arguments to be passed simultaneously
    parsed_args = parser.parse_args()
    special_args = [parsed_args.build, parsed_args.bench, parsed_args.debug, parsed_args.test]
    if sum(special_args) > 1:
        raise ValueError("Too many arguments. Can only pass one type of argument at a time")
    return parsed_args

def main():
    args = parse_args()
    if args.build:
        build_code()
    elif args.test:
        test_code()
    elif args.bench:
        bench_code()
    elif args.debug:
        debug_code()
    else:
        run_code()

if __name__ == '__main__':
    runner()