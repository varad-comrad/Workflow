import argparse, subprocess, settings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs=1, type=str)
    parser.add_argument('-b' ,'--branch', default=settings.default_branch)
    args = parser.parse_args()

    subprocess.run('git add .', cwd='.', shell=True)
    subprocess.run(f'git commit -am {args.args}', cwd='.', shell=True)
    subprocess.run(f'git push -u origin {args.branch}', cwd='.', shell=True)

if __name__ == '__main__':
    main()

