#这是一个函数库，用来做数据预处理
import pandas as pd
from functiontool.getrelation import getrelation
from functiontool.templib import temp_stupid
import numpy as np
import collections
from gensim.models import Word2Vec
model = Word2Vec.load('item2vec_sg1_hs0_size128_window5_all.model')
def gen_average_vec(item_list):
    '''
    item_list: 一个list 没有元素为live id（str）
    return 列表中所有live向量的平均值向量
    '''
    vecs = np.array([model.wv[x] for x in item_list])
    user2vec = np.mean(vecs,0)
    return list(user2vec)

def get_live_vec(live_id):
    '''
    live_id: 一个live id(str)
    return 返回这个live的向量
    '''
    return model.wv[live_id]

def get_lives(live_od,num):
    '''
    live_od: 一个live id(str)
    num: 要求返回live的个数
    return 一个list 包含与live_od在表征空间中最相似的前num个live 的id
    '''
    h=model.similar_by_word(live_od,topn=num)
    return [x[0] for x in h]
def get_lives_from_vec(worlist,num):
    '''
    worlist: 一个list，其中的每个元素*不是*live的id，而是live的向量
    num:要求返回live的个数
    return 一个list 包含与worlist中的向量最相似的前num个live
    '''
    h=model.most_similar(positive= worlist,topn=num)
    return [x[0] for x in h]


def index_user(userlist):
    '''
    userlist: 一个用户list，list中的元素都是用户id（str）
    return (index2user,user2index)
    这个函数主要是建立从user id到整数值的映射，返回的是两个字典
    这么做的必要性在于，一般机器学习算法中，都是用int32作为索引值
    从字典的命名：index2user就是以整数值索引为字典键，user id 为值；user2index反之
    '''
    user2index=dict()
    index2user = dict()
    for i in userlist:
        user2index[i]=len(user2index)
    index2user = dict(zip(user2index.values(),user2index.keys()))
    return index2user,user2index       


def sample(num_neg_sample,fillist,vocabulary):
    '''
    num_neg_sample: int 负采样的个数
    fillist: list of live id 采样时，保证fillist中的live不会出现
    vocabulary: list of live id sorted by frequency descending一个live id 的列表，其中按照live在购买记录中的出现频次降序排序
    vocabulary[0]应该是出现频次最大的那个词
    return 它返回的是一个索引列表，不是live id 的列表，只要在vocabulary里索引就能取值
    文献参考alibaba在kdd2018发表的论文
    '''
    p=vocabulary
    D=len(p)
    sample=[]
    i=0
    while True:
        if i>=num_neg_sample:
            break
        r = np.random.uniform(low=0.0, high=1.0, size=1)
        index = int(np.ceil(np.power(D+1,r))-2)
        if p[index] not in fillist:
            sample.append(index)
            i+=1
        else:
            continue
    return sample

def load_corpus(filename,usertxt,exper=None):
    '''
    filename： 语料的文件名，文件形式参考corpus.txt
    exper: int 这个参数是用来限制返回的用户（记录）个数的
        之所以用了exper命名
        是因为你写好程序后想试试能不能跑通
        这时候不用加载所有数据，后面处理很慢的
        设置exper=100就只返回100个用户的数据
    usertxt: 文件名，该文件用来存filename文件中每一行对应的user_id
    return    （sentence_d,all_d,vali,user）
        sentence_d: 一个列表，列表中的元素是一个用户的够买live的id序列，但是去除了最新买的live(要用做验证/测试)
        all_d: 和sentence_d不同的，没有抹去最新买的live，列表内的元素为(liveid,frequency_count)按降序排列
        vali: 抹去的那个最新买的live都存在这里了，这是一个列表，列表中每个元素为对应用户的最新买的live
        user: 这个列表存用户id
    注意。以上四个返回的列表长度都是一样的（len（））
        因此user[i]这位用户的购买记录存在all_d[i]中
        最新买的live是vali[i],
        除了最新买的，剩下的都在sentence_d[i]
        也就是说，四个列表同一索引存了同一个用户的信息
    '''
    from functiontool.templib import temp_stupid
    stop = temp_stupid('G:/zhihuX/old/needuser.txt').read()
    f = open(filename,'r')
    sentence_d=[]
    all_d=[]
    vali=[]
    user=[]
    lines = f.readlines()
    f.close()
    if usertxt:
        users = temp_stupid(usertxt).read()
    if exper:
        lines=lines[:exper]
        if usertxt:
            users = users[:exper]
    ii=0
    for sentence in lines:
        sen=sentence.split()
        num=len(sen)
        #if True:
        if num>1 and (not users[ii] in stop):
            vali.append(sen[0])
            sentence_d.append(sen[1:])
            all_d.extend(sen)
            user.append(users[ii])
        ii+=1
    
    all_d=collections.Counter(all_d).most_common()
    return sentence_d,all_d,vali,user

def load_corpus_test(numm=40000):
    '''
    这个函数加载测试集语料
    改编自load_corpus()
    由于纯粹为了临时使用，有些应该变成参数的，但是都固化在里面了
    返回的和load_corpus()一样
    '''
    from functiontool.templib import temp_stupid
    # stop里的都是训练集
    stop = temp_stupid('G:/zhihuX/old/needuser.txt').read()+temp_stupid('./sample/dir.txt').read()
    
    filename = 'corpus_all.txt'
    usertxt = 'dir.txt'
    f = open(filename,'r')
    sentence_d=[]
    all_d=[]
    vali=[]
    user=[]
    lines = f.readlines()
    f.close()
    users = temp_stupid(usertxt).read()
    ii=0
    pp=0
    for sentence in lines:
        if pp>numm:
            break
        sen=sentence.split()
        num=len(sen)
        #if True:
        if num>1 and (not users[ii] in stop):
            vali.append(sen[0])
            sentence_d.append(sen[1:])
            all_d.extend(sen)
            user.append(users[ii])
            pp+=1
        ii+=1
    
    all_d=collections.Counter(all_d).most_common()
    return sentence_d,all_d,vali,user


def generatecorpus():
    '''
    该函数生成corpus.txt形式的文件
    '''
    from functiontool.getrelation import getrelation
    from functiontool.templib import temp_stupid
    from functiontool.dirkit import getdir
    sample = getdir('G:/zhihuData/gooduser',pre='.txt')#该目录下为按用户存储（文件名为用户id）的内容
    from functiontool.kit import tranverse
    k=[]
    def a(i):
        k.append(' '.join(getrelation(i,path='G:/zhihuData')))
    tranverse(sample,a)
    temp_stupid('corpus_all.txt').update(k)



def index_item(itemlist):
    '''
    itemlist: 一个live list，list中的元素都是live id（str）
    return (index2user,user2index,itemlist)
    这个函数主要是建立从user id到整数值的映射，返回的是两个字典
    这么做的必要性在于，一般机器学习算法中，都是用int32作为索引值
    从字典的命名：index2item就是以整数值索引为字典键，live id 为值；live2index反之
    '''
    p=itemlist
    item2index=dict()
    index2item = dict()
    for i in p:
        item2index[i]=len(item2index)
    index2item = dict(zip(item2index.values(),item2index.keys()))
    return index2item,item2index,itemlist






