from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url=""
database= create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(bind=database)
session = Session()


def save_db():
    Base.metadata.create_all(bind=database)

