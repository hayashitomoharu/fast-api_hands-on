from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

# sqliteでの接続を作成

SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# テーブル定義

class Departments(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(length=10))

    __tablename__ = 'departments'

class Users(Base):

    id = Column(Integer, primary_key=True)
    user_name = Column(String(length=10))
    departments_id = Column(Integer,ForeignKey('departments.id'))

    __tablename__ = 'users'

# dbを作成

Base.metadata.create_all(bind=engine)


