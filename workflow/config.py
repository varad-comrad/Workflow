#!/usr/bin/env python
import json, pathlib, argparse, typing

# TODO: limit function to predefined keys
def set_value(key: typing.LiteralString, value: str | int) -> None:
    path = pathlib.Path(__file__).parent/'settings.json'
    with path.open('r') as file:
        s: dict = json.load(file)
    s[key] = value
    with path.open('w') as file:
        json.dump(s, file)

def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=2, type=str)
    return parser

def type_treating(key: str, value: str | int) -> tuple: 
    if key in ['db_port']:
        value = int(value)
    return key, value

def main():
    parser = make_parser()
    set_value(*(type_treating(*(parser.parse_args().args))))

if __name__ == '__main__':
    main()