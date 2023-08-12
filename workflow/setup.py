import json

with open('settings.json', 'w') as f:
    file = {"default_dir": "", "default_branch": "master", "venv_manager": "pyenv", "db_username": "",
            "db_password": 0, "path_to_sqlite": "db/data.db", "default_db_host": "localhost", "poetry_extension": "--src", "conda_extension": "-y", "pyenv_extension": ""}
    json.dump(file, f)