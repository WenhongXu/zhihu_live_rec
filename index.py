import functiontool as fu
from functiontool.orm import engine
from functiontool.dirkit import getdir
import pandas as pd

record = fu.recorder()

# se=list(pd.read_sql('user',engine)['id'])
have = list(getdir('G:/zhihuData/gooduser',pre='.txt'))
# filfunc=lambda x: True if x in se else False
# target=list(filter(filfunc,have))

from functiontool.easyRelation import *
from functiontool.getrelation import getrelation
# new('user','int')
# ea=easyRelation('user')
p = list(enumerate(have,1))
k=[]
def a(i):
    #ea.insert({'id':i[1],'token':i[0],'isprocess':len(getrelation(i[1],get='live',path='G:/zhihuData'))})
    num = len(getrelation(i[1],get='live',path='G:/zhihuData'))
    k.append(','.join([i[1],str(i[0]),str(num)]))
from functiontool.kit import tranverse
tranverse(p,a)
# ea.end()
from functiontool.templib import temp_stupid
temp_stupid('usermap.csv').update(k)
record.login(来源='zhihuData中的所有数据',输出='usermap.csv',内容='将user的id映射为int值，以便算法使用，同时在isprocess字段保存了涉及的live数量,是为了导入sqlite',设计工具='temolib,tranverse(in kit)')
record.wri('将user的id映射为int值的文件准备')