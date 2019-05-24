import pkuseg as pk
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import jieba
#文本处理模块

def gettext(html):
    '''
    去除html字符
    '''
    return BeautifulSoup(html,'html.parser').text.replace(' ','')

def text2list(text,stopwords):
    '''
    分词+停用词
    '''
    # seg=pk.pkuseg()
    li=jieba.cut(text)
    p=lambda x:True if x not in stopwords else False
    return list(filter(p,li))

def getfrequency(li):
    '''
    按词频排序
    '''
    a,b=np.unique(np.array(li),return_counts=True)
    return pd.DataFrame({'words':a,'frequency':b}).sort_values(['frequency'],ascending=False)

