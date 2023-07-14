#!/usr/bin/env python

import argparse, pathlib, dbsettings, subprocess


def db_parser():

    databases: list[str] = ['sqlite', 'mongodb', 'postgre', 'mysql', 'microsoftsql'] 

    parser = argparse.ArgumentParser()
    
    parser.add_argument('args', type=str, nargs=1)
    parser.add_argument('-db', '--database', required=True, type=str, choices=databases)
    parser.add_argument('-d', '--dir', default='.', type=str)
    parser.add_argument('-U', '--user', type=str)
    parser.add_argument('-pwd', '--password', type=str)
    parser.add_argument('-n', '--database-name', required=True, type=str)

    return parser

class DatabaseCreator:
    def __init__(self, parsed_args: argparse.ArgumentParser) -> None:
        self._db: str = parsed_args.database
        self._dir: pathlib.Path = pathlib.Path(parsed_args.dir)
        self._dir = self._dir.joinpath(f'{parsed_args.args[0]}')
        self._dir.mkdir(parents=True)

    def create_database(self):
        conf = self._dir.joinpath('conf') 
        conf.mkdir()
        models = self._dir.joinpath('models')
        models.mkdir()

        with self._dir.joinpath('requirements.txt').open('w') as requirements_file:
            pass
        with self._dir.joinpath('create_main.py').open('w') as create_main_file:
            create_main_file.write(dbsettings.create_main)
        with conf.joinpath('db_session.py').open('w') as db_session_file:
            db_session_file.write(dbsettings.db_session.format('something',
                                                                'other stuff',
                                                                self._db, 
                                                                'user', 
                                                                'password', 
                                                                dbsettings.databases_ports[self._db], 
                                                                'namedb'))
        models.joinpath('__all_models.py').touch()
        with models.joinpath('model_base.py').open('w') as model_base_file:
            model_base_file.write(dbsettings.model_base)


if __name__ == '__main__':
    DatabaseCreator(db_parser().parse_args()).create_database()

        
