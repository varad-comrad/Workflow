
import json, pathlib

if __name__ == 'settings':
    path = pathlib.Path(__file__)
    with path.parent.joinpath('settings.json').open('r') as settings_file:
        s = json.load(settings_file)
    default_dir = s['default_dir']
    default_branch = s['default_branch']
    venv_manager = s['venv_manager']
    db_username = s['db_username']
    db_password = s['db_password']
    path_to_sqlite = s['path_to_sqlite']
    default_db_host = s['default_db_host']
    default_text_editor = s.get('default_text_editor', 'vscode')
