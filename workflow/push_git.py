#!/usr/bin/env python
import argparse, subprocess, logging

logging.basicConfig(level=logging.INFO,
                    format="\x1b[38;5;20m[commit]\x1b[92m %(message)s\x1b[0m")



def branch_exists(branch: str) -> bool:
    lines = subprocess.run(
        'git branch -a', cwd='.', shell=True, capture_output=True, text=True).stdout.strip().splitlines()
    aux = [line.strip() for line in lines]
    return (('* ' + branch) in aux)
    #     return ''
    # else:
    #     return '-b'

def stash(message):
    subprocess.run(f'git stash save "stashed {message}"', cwd='.', shell=True)
    pass

def unstash_and_checkout(message):
    subprocess.run(f'git checkout {message}', cwd='.', shell=True)
    subprocess.run(f'git stash pop', cwd='.', shell=True)
    commit_changes(message)

def git_push(branch, extension=''):
    subprocess.run(f'git push -u origin {branch}', cwd='.', shell=True)

def git_add(files):
    if len(files) > 0:
        subprocess.run(f'git add {" ".join(files)}', cwd='.', shell=True)
    else:
        subprocess.run(f'git add .', cwd='.', shell=True)
    
def git_commit(message):
    subprocess.run(f"git commit -m '{message}'",cwd='.', shell=True)

def commit_changes(message, files=None):
    git_add(files or [])
    git_commit(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=1, type=str)
    parser.add_argument('-b' ,'--branch', default='')
    parser.add_argument('-f' ,'--files', default='', nargs='*', type=str)
    args = parser.parse_args()
    
    current_branch = subprocess.run(
        'git branch', shell=True, capture_output=True, text=True).stdout.split('*')[1].strip().split('\n')[0]
    
    if branch_exists(args.branch):
        stash(args.args)
        unstash_and_checkout(args.args)
        git_push(args.branch)
        return
    commit_changes(args.args[0], args.files)
    extension = '-b' if not branch_exists(args.branch) else ''
    git_push(current_branch, extension)
    if args.branch:
        current_branch = args.branch
        subprocess.run(f'git checkout {extension} {args.branch} && git push -u origin {current_branch}', cwd='.', shell=True)
    else:
        subprocess.run(f'git push -u origin {current_branch}', cwd='.', shell=True)

    logging.info(f"Committing on branch {current_branch}")
    


if __name__ == '__main__':
    main()

