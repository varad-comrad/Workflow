db_session = '''import sqlalchemy as sa
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
import pathlib
from models.model_base import ModelBase

__engine: Engine | None = None

def create_engine(sqlite: bool=False) -> Engine:
    global __engine
    if __engine:
        return __engine
    if sqlite:
        path = pathlib.Path('{}') #! variable here
        path.parent.mkdir(parents=True, exist_ok=True) 
        conn_str = f'sqlite:///' + str(path)
        __engine = sa.create_engine(url=conn_str, echo=False)
    else:
        conn_str = '{}://{}:{}@{}:{}/{}'  # ! variable here
        __engine = sa.create_engine(url=conn_str, echo=False)
    return __engine

def create_session() -> Session:
    global __engine
    if not __engine:
        create_engine({}) #! variable here
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()
    return session


def create_tables() -> None:
    global __engine
    if not __engine:
        create_engine({}) #! variable here
    import models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)

'''

model_base = '''import sqlalchemy.ext.declarative as decl

ModelBase = decl.declarative_base()
'''

create_main='''from conf.db_session import create_tables


if __name__ == '__main__':
    create_tables()
'''

databases_ports: dict = {
    'postgres': 5432,
    'sqlite': None
}