import numpy as np
from functiontool.getrelation import getrelation
from functiontool.dirkit import getdir
from sklearn import metrics
from load_data import *

#为二分类模型建立数据集
print('开始注册')
sentences,words,validatewords,user = load_corpus('corpus.txt',usertxt='./sample/dir.txt')
index2item,item2index,vocabulary=index_item(words)
index2user,user2index = index_user(user)
user_num = len(user)
#加载基本信息
live_base= pd.read_csv('live_base_all.csv',header=0,index_col='id')
user_base = pd.read_csv('user_base_all.csv',header=0,index_col='id')
distance = np.load('distance.npy')
print('基本信息加载完成')
#构造数据集
def live_vec(live_id):
    '''
    得到一个live的vector
    '''
    vec = list(get_live_vec(live_id))
    # side_information = list(live_base.loc[int(live_id)])
    vec = vec#+side_information
    return vec

def gen_user_average_vec(live_list):
    '''
    求一群live向量的平均值
    '''
    vecs = np.array([live_vec(x) for x in live_list])
    user2vec = np.mean(vecs,0)
    return list(user2vec)

def get_max(seed):
    '''
    在距离矩阵中找到距离seed指定live最远的live
    '''
    seedi = item2index[seed]
    q = np.argmin(distance[seedi])
    return index2item[q],q
    
def gen_user_attention_vec(live_list,live):
    num = len(live_list)
    livee=get_live_vec(live)
    d=len(livee)
    matric = np.array([get_live_vec(x) for x in live_list])#num*d
    target_live = np.array(get_live_vec(live)).reshape((d,1))
    weight = np.matmul(matric,target_live)
    weight = weight-np.max(weight)
    m_exp = np.exp(weight)
    sum_exp = np.sum(m_exp)
    weight = m_exp/sum_exp
    aver = np.matmul(weight.T,matric).reshape(d)
    return list(aver)
 
def gene_indivi_vec(index):
    '''
    生成一个用户的向量
    '''
    lines = sentences[index]
    #pool_average
    pool_vec = gen_user_average_vec(lines)# 平均向量
    # price_std = [np.array([float((live_base.loc[int(x)])['fee']) for x in lines]).std()]
    # side_information = list(user_base.loc[user[index],])
    vec = pool_vec#+price_std+side_information
    return vec

def gene_indivi_attention_vec(index,live):
    '''
    生成一个用户的向量，但是采用注意力加权机制
    '''
    lines = sentences[index]
    #pool_average
    pool_vec = gen_user_attention_vec(lines,live)# 平均向量
    # price_std = [np.array([float((live_base.loc[int(x)])['fee']) for x in lines]).std()]
    # side_information = list(user_base.loc[user[index],])
    vec = pool_vec#+price_std+side_information
    return vec

def gene_data():
    posi_data=[]
    nega_data=[]
    for i in range(user_num):
        print('get data'+str(i))
        #i 是用户标识
        posi_data.append(gene_indivi_vec(i)+live_vec(validatewords[i]))
        nega_data.append(gene_indivi_vec(i)+live_vec(get_max(validatewords[i])[0]))
    return posi_data,nega_data
print('开始构建数据')
posi_data,nega_data=gene_data()
print('数据构建完成')

np.savez('for_doubel_aver_no_side.npz',posi_data=posi_data,nega_data = nega_data)



