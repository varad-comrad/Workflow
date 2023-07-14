#!/usr/bin/env python
import argparse, pathlib, dbsettings, subprocess, settings


def db_parser() -> argparse.ArgumentParser:

    # databases: list[str] = ['sqlite', 'mongodb', 'postgre', 'mysql', 'microsoftsql'] 

    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    
    parser.add_argument('args', type=str, nargs=1)
    parser.add_argument('-db', '--database', required=True, type=str) # choices=databases
    parser.add_argument('-d', '--dir', default='.', type=str)
    parser.add_argument('-U', '--user', type=str, default=settings.db_username)
    parser.add_argument('-pwd', '--password', type=str, default=settings.db_password)
    parser.add_argument('-n', '--database-name', required=True, type=str)
    parser.add_argument('-p', '--port', type=int, default=None)
    parser.add_argument('-P', '--path-to-sqlite', type=str, default=settings.path_to_sqlite)

    return parser

class DatabaseCreator:
    def __init__(self, parsed_args: argparse.Namespace) -> None:
        self._db: str = parsed_args.database
        self._dir: pathlib.Path = pathlib.Path(
            parsed_args.dir)/f'{parsed_args.args[0]}'
        self._dir.mkdir(parents=True)
        self._parsed_args = parsed_args

    def create_database(self):
        conf = self._dir/'conf' 
        conf.mkdir()
        models = self._dir/'models'
        models.mkdir()

        # with self._dir.joinpath('requirements.txt').open('wb') as requirements_file:
        #     requirements_file.write(subprocess.check_output('pip freeze', shell=True))
        with self._dir.joinpath('create_main.py').open('w') as create_main_file:
            create_main_file.write(dbsettings.create_main)
        with conf.joinpath('db_session.py').open('w') as db_session_file:
            db_session_file.write(dbsettings.db_session.format(self._parsed_args.path_to_sqlite,
                                                               self._db, 
                                                               self._parsed_args.user, 
                                                               self._parsed_args.password,
                                                               self._parsed_args.port or dbsettings.databases_ports[self._db], 
                                                               self._parsed_args.database_name)
                                                               )
        models.joinpath('__all_models.py').touch()
        with models.joinpath('model_base.py').open('w') as model_base_file:
            model_base_file.write(dbsettings.model_base)


if __name__ == '__main__':
    args = db_parser().parse_args()
    if args.password is None and args.database != 'sqlite':
        raise ValueError('password must be specified')
    DatabaseCreator(args).create_database()

        
