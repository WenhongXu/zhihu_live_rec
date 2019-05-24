import sys
import logging
import os
import gensim
# 引入doc2vec
from gensim.models import Doc2Vec
from load_data import *
from functiontool.baseinfo import getlive
from functiontool.templib import temp_stupid
from functiontool.textpro import *
from functiontool.getrelation import *
import random

documents=[]
_,words,validatewords,user = load_corpus('corpus_all.txt',usertxt='dir.txt')
_,_,vocabulary=index_item(words)
stop = temp_stupid("G:/stopwords-master/stopwords.txt").read()
stop=[x.strip() for x in stop]
print(stop[:30])
# fil=lambda x:False if x in stop else True
for j in user:
    text = []
    for i in getrelation(j,path='G:/zhihuData')[1:]:
        x=None
        try:
            x=getlive(i).description
            # print(i)
            x = text2list(gettext(x),stop)
            # print(x[:10])
            text.extend(x)
            if not x:
                continue   
        except:
            print('ssssssssssss')
            continue
    try:        
        print(random.sample(text,10)) 
    except:
        pass   
    documents.append(gensim.models.doc2vec.TaggedDocument(text, [str(j)]))

model = Doc2Vec(documents, dm=1, size=128, window=8, min_count=5, workers=2)
# 保存模型
model.save('doc2vec_for_user_all.model')

