import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from load_data import *
# model = Word2Vec.load("item2vec_sg1_hs0_size128_window5_all.model")
sentences,words,validatewords,user = load_corpus('corpus_all.txt',usertxt='dir.txt')
index2item,item2index,vocabulary=index_item(words)
# mat=[]
# for i in range(len(vocabulary)):
#     assert i==item2index[vocabulary[i]]
#     mat.append(list(model.wv[vocabulary[i]]))
# distance = cosine_similarity(mat)
def get_max(seed):
    distance = np.load('distance.npy')
    seedi = item2index[seed]
    q = np.argmin(distance[seedi])
    return index2item[q],q

    
