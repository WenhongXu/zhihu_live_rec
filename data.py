#这是用来给youtube2016那篇论文的模型构造数据用的，我也跑了一遍，但是效果奇差。。。
import tensorflow as tf
import numpy as np
import pandas as pd
import random
from functiontool.getrelation import getrelation
from functiontool.dirkit import getdir
from functiontool.baseinfo import getlive
from sklearn import metrics
import math
from load_data import load_corpus,index_item,get_live_vec



sentences,words,validatewords,user = load_corpus('corpus.txt',usertxt='./sample/dir.txt')
assert len(sentences)==len(user)
index2item,item2index,vocabulary=index_item(words)
user_num = len(sentences)
item_num = len(words)
vocabulary_size=len(vocabulary)
print(vocabulary_size)
# sentences : 序列中的元素为live原始id
# words:  按热度排序的live列表,带有词频率，所以是个元组
# validatewords:  选取最后的几个作为抹去的对象，这些对象作为验证集使用
# user: 和sentences索引对应的用户id列表
# vocabulary： 按词频排序的列表

#已经获取了所有的索引信息，至此，数据集索引加载完成,且没有划分
print('所有内容报名完成，下面开始加载数据')

#下面加载基本信息


live_base= pd.read_csv('live_base_all.csv',header=0,index_col='id')
user_base = pd.read_csv('user_base_all.csv',header=0,index_col='id')
print('基本信息加载完成')
# _base：  都是使用df,index是id

train_num = int(user_num*0.8) 

#下面开始构造数据集
print('训练数据集构造开始'+str(train_num))

def live_vec(live_id):
    '''
    得到一个live的
    '''
    vec = list(get_live_vec(live_id))
    side_information = list(live_base.loc[int(live_id)])
    vec = vec+side_information
    return vec

def gen_user_average_vec(live_list):
    vecs = np.array([live_vec(x) for x in live_list])
    user2vec = np.mean(vecs,0)
    return list(user2vec)
    

def gene_indivi_vec(index):
    lines = sentences[index]
    #pool_average
    pool_vec = gen_user_average_vec(lines)# 平均向量
    price_std = [np.array([float((live_base.loc[int(x)])['fee']) for x in lines]).std()]
    side_information = list(user_base.loc[user[index],])
    vec = pool_vec+price_std+side_information
    return vec

def gene_data():
    data_u=[]
    labels=[]
    for i in range(user_num):
        print('get data'+str(i))
        #i 是用户标识
        data_u.append(gene_indivi_vec(i))
        labels.append(item2index[validatewords[i]])
    return data_u,labels

data,labels=gene_data()




print('测试训练集构造完成')
np.savez('for_youtube_like_NEW.npz',data=np.array(data,dtype=np.float32),
    labels=np.array(labels,dtype=np.float32))