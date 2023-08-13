import json, pathlib, subprocess


# ask for user input here
def initial_configs():
	with open('settings.json', 'w') as f:
		file = {"default_dir": "", "default_branch": "master", "venv_manager": "pyenv", "db_username": "",
				"db_password": 0, "path_to_sqlite": "db/data.db", "default_db_host": "localhost", "poetry_extension": "--src", "conda_extension": "-y", "pyenv_extension": ""}
		json.dump(file, f)

def create_workflow_directory():
	home = pathlib.Path(f'/home/{subprocess.run("whoami", shell=True)}')
	try:
		(home / '.workflow').mkdir(exist_ok=False)
	except:
		print("Could not setup workflow, a folder with name .workflow already exists")
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
			rc.write(f'\n\nPATH =$PATH: ~/.workflow/workflow\nsource ~/.workflow/workflow/scripts.zsh\n\n')

