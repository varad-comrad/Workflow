#!/usr/bin/env python

import pathlib, subprocess, glob, sys, argparse, logging, json


def run(path:pathlib.Path):
    if path.is_file():
        return run_file(path)
    else:
        return run_dir(path)
    

def run_file(path:pathlib.Path):
    extension = path.name.split('.')[-1]
    data: dict
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['FileExecutorMap']
    if extension not in data.keys():
        raise ValueError(f'No runner found for extension {extension}')
    command: str = data[extension]
    to_format: list[str]
    
    if extension in ['c', 'cpp']:
        to_format = [path.name, path.name.split(
            '.')[0], path.name.split('.')[0]]        
    elif extension in ['rs', 'java', 'kt']:
        to_format = [path.name, path.name.split('.')[0]]
    else:
        to_format = [path.name]

    command = command.format(*to_format)
    process = subprocess.run(f'cd {path.parent.absolute()} && ' + command, shell=True, capture_output=True, text=True)
    try:
        return process.stdout.strip()
    except subprocess.CalledProcessError:
        return process.stderr.strip()

def run_dir(path:pathlib.Path):
    pass

def run_code(path: pathlib.Path):
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
    args = pathlib.Path(parse_args().args)
    return run_file(args)
    # if args.build:
    #     build_code()
    # elif args.test:
    #     test_code()
    # elif args.bench:
    #     bench_code()
    # elif args.debug:
    #     debug_code()
    # else:
    #     run_code()

if __name__ == '__main__':
    print(main())