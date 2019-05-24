#from py2neo import Graph
#from functiontool.ogm import Live,Person
from functiontool.templib import temp_stupid
import json

# try:
#     gb = Graph("bolt://localhost:7687", auth=('neo4j', '19971012'))
# except:
#     pass

# def getrelation(id,get='live'):
#     if get == 'live':
#         return [i.id for i in Person.match(gb,id).first().participate]
#     elif get == 'person':
#         return [i.id for i in Live.match(gb,id).first().participate]

def getrelation(id,get='live',path='.'):
    '''
    返回一个live的所有用户
    或
    返回一个用户的所有live
    内容都来自数据库
    '''
    if get == 'live':
        return [json.loads(i.replace('\'','\"'))['id'] for i in temp_stupid(path+'/gooduser/'+id+'.txt').read()]
    elif get == 'person':
        return temp_stupid(path+'/goodlive/'+id+'.txt').read()

