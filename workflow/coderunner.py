#!/usr/bin/env python

import pathlib, subprocess, argparse, logging, json, time


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def custom_log(level, message):
    if level == logging.INFO:
        formatted_message = f"\x1b[38;5;20m[Running]\x1b[92m {message}\x1b[0m"
    elif level == logging.WARNING:
        formatted_message = f"\033[38;5;20m[Done]\x1b[92m {message}\x1b[0m"
    elif level == logging.ERROR:
        formatted_message = f"\033[31m[ERROR]\x1b[92m {message}\x1b[0m"
    else:
        formatted_message = message
    logger.log(level, formatted_message)


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
    return command, path

def run_dir(path:pathlib.Path):
    data: dict
    command: str
    aux_file: str
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['DirectoryExecutorMap']
    for element in path.iterdir():
        if (aux_file := element.name) in data.keys():
            command = data[aux_file]
            break
    else:
        raise ValueError("innapropriate")

    to_format: list[str]
    if aux_file in ['main.py', '__main__.py', 'pyproject.toml']:
        to_format.append(path.name)
    return command, path

def debug_code(path: pathlib.Path):
    if path.is_file():
        return debug_file(path)
    else:
        return debug_dir(path)

def debug_file(path: pathlib.Path):
    pass

def debug_dir(path: pathlib.Path):
    data: dict
    command: str
    aux_file: str
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['DirectoryDebugMap']
    for element in path.iterdir():
        if (aux_file := element.name) in data.keys():
            command = data[aux_file]
            break
    else:
        raise ValueError("innapropriate")

    to_format: list[str]
    if aux_file in ['main.py', '__main__.py', 'pyproject.toml']:
        to_format.append(path.name)
    return command, path

def test_code(path: pathlib.Path):
    data: dict
    command: str
    aux_file: str
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['DirectoryTestMap']
    for element in path.iterdir():
        if (aux_file := element.name) in data.keys():
            command = data[aux_file]
            break
    else:
        raise ValueError("innapropriate")

    to_format: list[str]
    if aux_file in ['main.py', '__main__.py', 'pyproject.toml']:
        to_format.append(path.name)
    return command, path

def bench_code(path: pathlib.Path):
    data: dict
    command: str
    aux_file: str
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['DirectoryBenchMap']
    for element in path.iterdir():
        if (aux_file := element.name) in data.keys():
            command = data[aux_file]
            break
    else:
        raise ValueError("innapropriate")

    to_format: list[str]
    if aux_file in ['main.py', '__main__.py', 'pyproject.toml']:
        to_format.append(path.name)
    return command, path

def build_code(path: pathlib.Path):
    if path.is_file():
        return build_file(path)
    else:
        return build_dir(path)

def build_file(path: pathlib.Path):
    extension = path.name.split('.')[-1]
    data: dict
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['FileBuildMap']
    if extension not in data.keys():
        raise ValueError(f'No runner found for extension {extension}')
    command: str = data[extension]
    to_format: list[str]

    if extension in ['c', 'cpp']:
        to_format = [path.name, path.name.split('.')[0]]
    else:
        to_format = [path.name]

    command = command.format(*to_format)
    return command, path

def build_dir(path: pathlib.Path):
    data: dict
    command: str
    aux_file: str
    with (pathlib.Path(__file__).parent / 'runner.json').open('r') as file:
        data = json.load(file)['DirectoryBuildMap']
    for element in path.iterdir():
        if (aux_file := element.name) in data.keys():
            command = data[aux_file]
            break
    else:
        raise ValueError("innapropriate")

    to_format: list[str]
    if aux_file in ['main.py', '__main__.py', 'pyproject.toml']:
        to_format.append(path.name)
    return command, path

def executor(command: str, path: pathlib.Path):
    code = 0
    try:
        custom_log(logging.INFO,f'cd {path.parent.absolute()} && {command}')
        t0 = time.perf_counter()
        result = subprocess.run(command, cwd=path.parent.absolute(
        ), shell=True, capture_output=True, text=True)
        output = result.stdout.strip()
        err_output = result.stderr.strip()
        code = result.returncode
        print(output, err_output, sep='\n\n')

    except subprocess.CalledProcessError as e:
        code = e.returncode
        print(e.stdout, e.stderr, sep='\n\n')
    finally:
        ansi_code: str
        ansi_code2 = '\033[35m'
        ansi_code3 = '\x1b[92m'
        if code == 0:
            ansi_code = '\033[35m'
        else:
            ansi_code = '\033[31m'
        custom_log(logging.WARNING,
            f"exited with {ansi_code}{code=}{ansi_code3} in {ansi_code2}{(time.perf_counter() - t0):.3f}{ansi_code3} seconds")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', type=str, default='.')
    parser.add_argument('--build', action='store_true', default=False)
    parser.add_argument('--test', action='store_true', default=False)
    parser.add_argument('--bench', action='store_true', default=False)
    parser.add_argument('--debug', action='store_true', default=False)
    parsed_args = parser.parse_args()
    special_args = [parsed_args.build, parsed_args.bench, parsed_args.debug, parsed_args.test]
    if sum(special_args) > 1:
        raise ValueError("Too many arguments. Can only pass one type of argument at a time")
    return parsed_args

def main():
    parsed_args = parse_args()
    args = pathlib.Path(parsed_args.args)
    
    if parsed_args.build:
        executor(*build_code(args))
    elif parsed_args.test:
        executor(*test_code(args))
    elif parsed_args.bench:
        executor(*bench_code(args))
    elif parsed_args.debug:
        executor(*debug_code(args))
    else:
        executor(*run(args))

if __name__ == '__main__':
    main()