from database import Base 
from sqlalchemy import Column, Integer, String 

class Item(Base):
    __tablename__="tasks"

    id=Column(Integer,primary_key=True, index=True)
    name = Column(String,index=True)
    description = Column(String)

    