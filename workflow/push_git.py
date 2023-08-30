#!/usr/bin/env python
import argparse, subprocess, logging

logging.basicConfig(level=logging.INFO,
                    format="\x1b[92m[%(levelname)s] %(message)s\x1b[0m")



def branch_exists(branch: str) -> str:
    lines = subprocess.run(
        'git branch -a', cwd='.', shell=True, capture_output=True, text=True).stdout.strip().splitlines()
    aux = [line.strip() for line in lines]
    if ('* ' + branch) in aux:
        return ''
    else:
        return '-b'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=1, type=str)
    parser.add_argument('-b' ,'--branch', default='')
    parser.add_argument('-f' ,'--files', default='', nargs='*', type=str)
    args = parser.parse_args()
    
    current_branch = subprocess.run(
        'git branch', shell=True, capture_output=True, text=True).stdout
    print(current_branch.split('*')[1].strip())
    current_branch = current_branch.split('*')[1].strip()
    
    if len(args.files) > 0:

        subprocess.run(f'git add {" ".join(args.files)}', cwd='.', shell=True)
        pass
    else:
        subprocess.run(f'git add .', cwd='.', shell=True)
    
    subprocess.run(f"git commit -m '{args.args[0]}'",cwd='.', shell=True)
    
    if args.branch:
        current_branch = args.branch
        subprocess.run(f'git checkout {branch_exists(args.branch)} {args.branch} && git push -u origin {current_branch}', cwd='.', shell=True)
    else:
        subprocess.run(f'git push -u origin {current_branch}', cwd='.', shell=True)

    logging.info(f"Committing on branch {current_branch}")
    


if __name__ == '__main__':
    main()

