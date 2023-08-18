#!/usr/bin/env python
import json, pathlib, argparse, typing

# TODO: limit function to predefined keys
def set_value(key: typing.LiteralString, value: str | int) -> None:
    path = pathlib.Path(__file__).parent/'settings.json'
    with path.open('r') as file:
        s: dict = json.load(file)
    if key == 'remove':
        s.pop(value, None)
    else:
        s[key] = value
    with path.open('w') as file:
        json.dump(s, file)

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=2, type=str)
    parser.add_argument('--show-all', action='store_true', default=False)
    parser.add_argument('--show', type=str, default=False)
    return parser

def type_treating(key: str, value: str | int) -> tuple: 
    if key in ['db_port']:
        value = int(value)
    return key, value

def show_all_args() -> None:
    path = pathlib.Path(__file__).parent/'settings.json'
    with path.open('r') as file:
        s = json.load(file)
        print(s)

def show_arg(arg: str) -> None:
    path = pathlib.Path(__file__).parent/'settings.json'
    with path.open('r') as file:
        s = json.load(file)
        print(s.get(arg, 'Not defined'))

def main():
    parsed_args = make_parser().parse_args()
    if parsed_args.show_all:
        show_all_args()
    elif parsed_args.show != '':
        show_arg(parsed_args.show)
    else:
        set_value(*(type_treating(*(parsed_args.args))))

if __name__ == '__main__':
    main()