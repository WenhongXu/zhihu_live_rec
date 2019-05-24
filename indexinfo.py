from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,Boolean,Date,Float,Text,CHAR
from sqlalchemy.orm import sessionmaker, relationship
engine1 = create_engine('sqlite:///live.db')
engine2 = create_engine('sqlite:///user.db')
Base_live = declarative_base(bind=engine1)
Base_user = declarative_base(bind=engine2)
class LIVEINDEX(Base_live):
    __tablename__ = 'id2token'
    id = Column(String(100),primary_key=True)
    token =Column(Integer())
    isprocess=Column(Integer())

class USERINDEX(Base_user):
    __tablename__ = 'id2token'
    id = Column(String(100),primary_key=True)
    token =Column(Integer())
    isprocess=Column(Integer())
Session_live = sessionmaker(bind=engine1)
session_live = Session_live()
Session_user = sessionmaker(bind=engine2)
session_user = Session_user()

def get_users(cond,num):
    if cond=='>':
        x=session_user.query(USERINDEX).filter(USERINDEX.isprocess>=num).all()
    elif cond=='<':
        x=session_user.query(USERINDEX).filter(USERINDEX.isprocess<=num).all()
    return [p.id for p in x]

def get_lives(cond,num):
    if cond=='>':
        x=session_live.query(LIVEINDEX).filter(LIVEINDEX.isprocess>=num).all()
    elif cond=='<':
        x=session_live.query(LIVEINDEX).filter(LIVEINDEX.isprocess<=num).all()
    return [p.id for p in x]


