import json, pathlib, subprocess


# ask for user input here
def initial_configs():
	with open('settings.json', 'w') as f:
		file = {"default_dir": "", "default_branch": "master", "venv_manager": "pyenv", "db_username": "",
				"db_password": 0, "path_to_sqlite": "db/data.db", "default_db_host": "localhost", "poetry_extension": "--src", "conda_extension": "-y", "pyenv_extension": ""}
		json.dump(file, f)

def create_workflow_directory():
	home = pathlib.Path(f'/home/{subprocess.run("whoami", shell=True)}')
	name = '.workflow'
	while True:
		try:
			(home / name).mkdir(exist_ok=False)
			break
		except:
			print(f"Could not setup workflow, a folder with name {name} already exists")
			name = input("Write the name you wish for it")

	rcs = []
	for element in home.iterdir():
		if element == '.zshrc':
			rcs.append(home / '.zshrc')
		if element == '.fishrc':
			rcs.append(home / '.fishrc')
		if element == '.bashrc':
			rcs.append(home / '.bashrc')
		if element == '.zshrc':
			rcs.append(home / '.zshrc')

	for rc in rcs:
		with rc.open('a') as file:
			rc.write(f'\n\nPATH =$PATH: ~/{name}/workflow\nsource ~/{name}/workflow/scripts.zsh\n\n')

def copy_workflow_dir():
	# Copy the workflow directory from the 'git clone' to the folder .workflow (or other one)
	pass

def main():
	pass

if __name__ == '__main__':
	main()
