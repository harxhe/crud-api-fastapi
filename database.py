from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL= "postgresql://postgres:7488439465@localhost:5432/testdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()