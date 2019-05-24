#训练模型
def generatecorpus():
    from functiontool.getrelation import getrelation
    from functiontool.templib import temp_stupid
    from functiontool.dirkit import getdir
    sample = getdir('G:/zhihuData/gooduser',pre='.txt')
    from functiontool.kit import tranverse
    k=[]
    def a(i):
        k.append(' '.join(getrelation(i,path='G:/zhihuData')))
    tranverse(sample,a)
    temp_stupid('corpus_all.txt').update(k)

from gensim.models import word2vec
sentences = word2vec.LineSentence('corpus_all.txt') 
model = word2vec.Word2Vec(sentences, sg=1,hs=0,min_count=1,window=5,size=128)
model.save("item2vec_sg1_hs0_size128_window5_all.model")
from functiontool import recorder
reco=recorder()
reco.login(输入='全部数据集',输出='item2vec_sg1_hs0_size128_window5.model',内容="使用有gensim封装的word2vec包,直接进行item2vec模型训练，并保存模型,模型信息在模型的命名中",预处理='将购买记录处理为sentence line的文件，不需要经过分词，该步使用了基本的到数据工具templib',问题='预处理花费了大量的时间')
reco.wri('第三次word2vec训练')

# if __name__=='__main__':
#     generatecorpus()