import json
import pathlib
import subprocess
import shutil


def create_workflow_directory() -> pathlib.Path:
	home = pathlib.Path(
		f'/home/{subprocess.run("whoami", shell=True,  capture_output=True, text=True).stdout.strip()}')
	name = '.workflow'
	while True:
		try:
			(home / name).mkdir(exist_ok=False)
			break
		except:
			print(f"Could not setup workflow, a folder with name {name} already exists")
			name = input("Write the name you wish for it: ")
	rcs = []
	for element in home.iterdir():
		if element.name == '.zshrc':
			rcs.append(home / '.zshrc')
		if element.name == '.fishrc':
			rcs.append(home / '.fishrc')
		if element.name == '.bashrc':
			rcs.append(home / '.bashrc')
		# if element == '.zshrc':
		# 	rcs.append(home / '.zshrc')

	for rc in rcs:
		with rc.open('a') as file:
			file.write(
				f'\n\nhome_dir_workflow=~/{name}\nPATH=$PATH: $home_dir_workflow\nsource $home_dir_workflow/scripts.zsh\n\n')
	return home/name


def move_directory(directory: pathlib.Path, destination: pathlib.Path):
	shutil.copytree(directory, destination, dirs_exist_ok=True)

# ask for user input here
def initial_configs(dir: pathlib.Path):
	...
	with (dir/'settings.json').open('w') as f:
		file = {"default_dir": "", "default_branch": "master", "venv_manager": "pyenv", "db_username": "",
			"db_password": 0, "path_to_sqlite": "db/data.db", "default_db_host": "localhost", "poetry_extension": "--src", "conda_extension": "-y", "pyenv_extension": ""}
		json.dump(file, f)


def chmod(dir: pathlib.Path, mode: int = 777):
	subprocess.run(f'sudo chmod {mode} {dir.absolute()}', shell=True)
	# dir.chmod(mode)
	for element in dir.iterdir():
		if element.is_dir():
			chmod(element, mode)
		element.chmod(mode)


def create_scripts_sh(dir: pathlib.Path):
	template = '''
function resetter(){
    if [ $1 = 'commit' ]; then
        shift
        reset_commit $@

    fi 
}

function reset_commit() {
  local commit_number=${1:-"1"}
  local commit_reference="HEAD~$commit_number"
  local commit_hash=$(git rev-parse "$commit_reference")
  git reset --hard "$commit_hash"
}

function workon(){
	local p=$1
    # TODO: create venv if doesn't exist
	source $1/bin/activate
}

function pythonproj(){
	msg=$(pyproj.py $@)
    vman=$(echo $msg | tail -n 1)
    eval $vman
}

function mkproj(){
	mkproj.py $@
}

function javaproj(){
	javaproj.py $@
}

function mkdb(){
    mkdb.py $@
}

function push_git(){
	push_git.py $@
}

function mkdirproj(){
	mkdirproj.py $@
}

function activate_shell(){
    shell.py 
}

function new_function(){
    make_workflow.py $@
}

function workflow(){

    if [ $# -eq 0 ]; then
        activate_shell
    elif [ $1 = 'config' ]; then
        shift
        config.py "$@" 
    elif [ $1 = 'mkdir' ]; then
        shift
        mkdirproj "$@" 
    elif [ $1 = 'pythonproj' ]; then
        shift
        pythonproj "$@" 
    elif  [ $1 = 'mkdb' ]; then
        shift
        mkdb "$@" 
    elif  [ $1 = 'push' ]; then
        shift
        push_git "$@" 
    elif [ $1 = 'new' ]; then
        shift
        new_function "$@"
    elif [ $1 = 'reset' ]; then
        shift
        resetter "$@"
    elif [ $1 = '-h' ]; then
        cat "$home_dir_workflow/text_files/advanced_helper.txt"
    else
        cat "$home_dir_workflow/text_files/helper.txt"
    fi

}
'''
	with (dir/ 'scripts.sh').open('w') as file:
		file.write(template)
	pass


def main():
	path = create_workflow_directory()
	move_directory(pathlib.Path('.') / 'workflow', path)
	initial_configs(path)
	chmod(path)
	create_scripts_sh(path)

if __name__ == '__main__':
	main()
