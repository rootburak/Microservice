from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = 'root'  
password = '12345'
database = 'blog'
host = 'localhost'
port = '3306'

db_url= f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

database= create_engine(db_url)
Base = declarative_base()
session = sessionmaker(bind=database)


def save_db():
    Base.metadata.create_all(bind=database)

