#!/bin/python

import argparse
import pathlib


def parse_args():

    databases: list[str] = ['sqlite', 'mongodb', 'postgre', 'mysql', 'microsoftsql'] 

    parser = argparse.ArgumentParser()
    
    parser.add_argument('args', type=str, nargs=1)
    parser.add_argument('-db', '--database', required=True, type=str, choices=databases)
    parser.add_argument('-d', '--dir', default='.', type=str)


    return parser.parse_args()

class DatabaseCreator:
    def __init__(self, parsed_args: argparse.Namespace) -> None:
        self._db: str = parsed_args.database
        self._dir: pathlib.Path = pathlib.Path(parsed_args.dir)
        self._dir = self._dir.joinpath(f'{parsed_args.args[0]}')
        self._dir.mkdir(parents=True)

    def create_sqlite(self):
        conf = self._dir.joinpath('conf') 
        conf.mkdir()
        models = self._dir.joinpath('models')
        models.mkdir()

        self._dir.joinpath('requirements.txt').touch()
        self._dir.joinpath('create_main.py').touch()
        conf.joinpath('db_session.py').touch()
        models.joinpath('__all_models.py').touch()
        models.joinpath('model_base.py').touch()

        def create_mongodb(self):
            pass

        def create_postgre(self):
            pass

        def create_mysql(self):
            pass

        def create_microsoft(self):
            pass

        def create_surreal(self):
            pass

if __name__ == '__main__':
    DatabaseCreator(parse_args()).create_sqlite()

        
