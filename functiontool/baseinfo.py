from functiontool.orm import *
from functiontool.constant import getRequest
from functiontool.tiny_spider import tiny_live,tiny_people
import json
Session = sessionmaker(bind=engine)
session = Session()

def getuser(id):
    x=session.query(PERSON).filter_by(id=id).all()
    if x:
        return x[0]
    else:
        return getuseronline(id)

def getlive(id):
    x=session.query(LIVE).filter_by(id=id).all()
    if x:
        return x[0]
    else:
        return getliveonline(id)


#下面的函数是为了应对数据库中没有信息的情况，没有的话，就直接用爬虫立即爬
def getliveonline(id):
    return FORWEB(json.loads(tiny_live(id,getRequest()),encoding='utf-8'))

def getuseronline(id):
    return FORWEB(json.loads(tiny_people(id,getRequest()),encoding='utf-8'))

def getalluser(ids):
    return session.query(PERSON).filter(PERSON.id.in_(ids)).all()


