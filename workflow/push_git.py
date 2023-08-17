#!/usr/bin/env python
import argparse, subprocess

def branch_exists(branch: str) -> str:
    lines = subprocess.run(
        'git branch -a', shell=True, capture_output=True, text=True).stdout.strip().splitlines()
    aux = [line.strip() for line in lines]
    if ('* ' + branch) in aux:
        return ''
    else:
        return '-b'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=1, type=str)
    parser.add_argument('-b' ,'--branch', default='')
    args = parser.parse_args()
    current_branch = subprocess.run(
        'git branch', shell=True, capture_output=True, text=True).stdout.split('*')[1].strip()
    subprocess.run(f'git add .', cwd='.', shell=True)
    subprocess.run(f"git commit -m '{args.args[0]}'",cwd='.', shell=True)
    if args.branch:
        current_branch = args.branch
        subprocess.run(f'git checkout {branch_exists(args.branch)} {args.branch} && git push -u origin {current_branch}', cwd='.', shell=True)
    else:
        subprocess.run(f'git push -u origin {current_branch}', cwd='.', shell=True)

if __name__ == '__main__':
    main()

