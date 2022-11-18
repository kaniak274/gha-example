import os
from contextlib import contextmanager

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    MetaData,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    os.environ["UNI_DATABASE_URI"],
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=100,
)
metadata = MetaData(engine)
Base = declarative_base()


class RandomDatabaseModel(Base):
    __tablename__ = "random_table"

    random_id = Column(Integer, primary_key=True)
    random_text = Column(String(255))


def get_session():
    return sessionmaker(autocommit=False, autoflush=True, bind=engine)()


@contextmanager
def session_scope():
    session = get_session()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def save_item(item):
    with session_scope() as session:
        session.add(item)
