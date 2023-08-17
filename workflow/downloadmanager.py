#!/usr/bin/env python

import argparse, time, shutil, subprocess, pathlib, json, logging

logging.basicConfig(level=logging.INFO,
                    format="\x1b[92m[%(levelname)s] %(message)s\x1b[0m")


def parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", nargs=2, type=str) # pattern and folder
    parser.add_argument("-d", "--add-dir", type=str, nargs='+') # add folder to watchlist
    parser.add_argument("-r", "--rm-dir", type=str, nargs='+') # remove folder from watchlist
    parser.add_argument("-l", "--loop", action='store_true', default=False)
    args = parser.parse_args()
    if args.loop and any([args.add_dir, args.rm_dir, args.config]):
        raise ValueError()
    return args

def open_file():
    content = {}
    with open(f'downloadmanager.json', 'r') as file:
        content = json.load(file)
    return content

def write_file(content):
    with open(f'downloadmanager.json', 'w') as file:
        json.dump(content, file)

def add_dir(new_dirs):
    content = open_file()
    content['watchlist'].extend(new_dirs)
    write_file(content)

def rm_dir():
    content = open_file()
    write_file(content)

def config():
    content = open_file()
    write_file(content)


def supervise() -> None:
    content = open_file()
    home = pathlib.Path(f"/home/{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}/")
    for directory in content['watchlist']:
        dir: pathlib.Path = home/directory
        for item in dir.iterdir():
            for terminal, dest in content['patterns'].items():
                if item.name.endswith('.' + terminal):
                    shutil.move(
                        item, f"/home/{subprocess.run('whoami', shell=True, capture_output=True, text=True).stdout.strip()}/{dest}")

def supervise_loop():
    try:
        while True:
            time.sleep(1)
            supervise()
    except KeyboardInterrupt:
        logging.info("Exiting process")
        time.sleep(0.5)

def main():
    args = parsed_args()
    if args.add_dir:
        pass
    if args.rm_dir:
        pass
    if args.config:
        pass
    if not any([args.add_dir, args.rm_dir, args.config]):
        if args.loop:
            supervise_loop()
        else:
            supervise()

if __name__ == "__main__":
    main()