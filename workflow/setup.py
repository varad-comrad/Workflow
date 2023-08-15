import json
import pathlib
import subprocess
import shutil
import argparse


def create_workflow_directory() -> pathlib.Path:
	home = pathlib.Path(
		f'/home/{subprocess.run("whoami", shell=True, capture_output=True, text=True).stdout.strip()}')
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
		if element == '.kshrc':
			rcs.append(home / '.kshrc')
		if element == '.cshrc':
			rcs.append(home / '.cshrc')
		if element == '.tcshrc':
			rcs.append(home / '.tcshrc')
		if element == '.dashrc':
			rcs.append(home / '.dashrc')

	for rc in rcs:
		with rc.open('a') as file:
			file.write(
				f'\n\nhome_dir_workflow=~/{name}\nPATH=$PATH:$home_dir_workflow\nsource $home_dir_workflow/scripts.sh\n\n')
	return home/name


def move_directory(directory: pathlib.Path, destination: pathlib.Path):
	shutil.copytree(directory, destination, dirs_exist_ok=True)

# ask for user input here
def initial_configs(dir: pathlib.Path):

	default_dir = input('Enter the absolute path to the default directory: ')
	default_branch = input('Enter the name of the default branch: ')
	venv_manager = input("Enter the name of the default Python's venv manager (pyenv, conda or poetry): ")
	home_dir = subprocess.run(
		'$home_dir_workflow', shell=True, capture_output=True, text=True).stdout.strip()

	with (dir/'settings.json').open('w') as f:
		file = {
			"default_dir": default_dir,
			"default_branch": default_branch, 
			"venv_manager": venv_manager, 
			"db_username": "",
			"db_password": 0, 
			"path_to_sqlite": "db/data.db", 
			"default_db_host": "localhost", 
			"poetry_extension": "--src", 
			"conda_extension": "-y", 
			"pyenv_extension": "",
			"home_dir": home_dir
		}
		json.dump(file, f)


def chmod(dir: pathlib.Path, mode: int = 777):
	subprocess.run(f'sudo chmod {mode} {dir.absolute()}', shell=True)
	# dir.chmod(mode)
	for element in dir.iterdir():
		if element.is_dir():
			chmod(element, mode)
		subprocess.run(f'sudo chmod {mode} {element.absolute()}', shell=True)


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
	local p=$(workon.py $@)
	eval $p
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

function new_workflow(){
    if [ $1 = 'function' ]; then
        shift
        make_workflow.py "$@"
    elif [ $1 = 'alias' ]; then
        shift
        alias.py "$@"        
    fi
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
        new_workflow "$@" 
    elif [ $1 = 'reset' ]; then
        shift
        resetter "$@"
    elif [ $1 = '-h' ]; then
        cat text_files/advanced_helper.txt
    else
        cat text_files/helper.txt 
    fi

}


'''
	with (dir/ 'scripts.sh').open('w') as file:
		file.write(template)
	pass

def check_pyenv_existence():
	pyenv_exists = True #TODO: develop proper check
	if not pyenv_exists:
		consent = input("Pyenv was not found. Do you wish to install it (Y/N)? ")
		if consent.lowercase == 'y':
			install_pyenv()
		else:
			return 
	
def check_conda_existence():
	pass

def check_poetry_existence():
	pass

def install_pyenv():
	subprocess.run(
		'git clone https://github.com/pyenv/pyenv.git ~/.pyenv && cd ~/.pyenv && src/configure && make -C src', shell=True)
	print('\n'*3)
	sh = input('write the name of the shell you want pyenv installed (bash, zsh, ...)')
	subprocess.run(
            f'''echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.{sh}rc
            echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.{sh}rc
            echo 'eval "$(pyenv init -)"' >> ~/.{sh}rc''', shell=True)

def install_poetry():
	pass

def install_conda():
	pass

def install_make():
	pass

def install_cargo():
	pass

def install_cmake():
	pass

def install_maven():
	pass

def install_gradle():
	pass

def install_jdk():
	pass

def install_kotlinc():
	pass

def install_distrobox():
	pass

def install_docker():
	pass

def install_julia():
	pass

def install_node():
	pass

def install_ts_node():
	pass

def install_nim():
	pass

def install_go():
	pass

def install_zig():
	pass

def install_v():
	pass

def install_cs():
	pass

def install_ruby():
	pass

def arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('--install-all', action='store_true', default=False)
	parser.add_argument('-y', action='store_true', default=False)
	parser.add_argument('--install', nargs='*', default=[])

def main():
	check_pyenv_existence()
	path = create_workflow_directory()
	move_directory(pathlib.Path('.') / 'workflow', path)
	chmod(path)
	initial_configs(path)
	create_scripts_sh(path)

if __name__ == '__main__':
	main()
