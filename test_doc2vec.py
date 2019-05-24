from gensim.models import Doc2Vec
from functiontool.baseinfo import getlive
from functiontool.textpro import gettext
model = Doc2Vec.load("doc2vec.model")
seed = '833695646706978816'
seeddd=getlive(seed)
print('种子live----'+seeddd.subject+'     '+str(seeddd.tags))
# print(gettext(seeddd.description))
print('\n')
for key in model.docvecs.most_similar(seed,topn =6):
    # print(key)
    tem=getlive(key[0])
    print(tem.subject+'\t'+str(tem.tags))
    # print(gettext(tem.description))
    print('===============')
# print(model.docvecs[seed])
# from gensim.models import Word2Vec
# from functiontool.baseinfo import getlive
# model = Word2Vec.load("item2vec_sg1_hs0_size32_window5_50k.model")
# # seed = '805554887650848768'
# seeddd=getlive(seed)
# print('初始情况----'+seeddd.subject+'     '+str(seeddd.tags))
# print('\n'+'标题\t分类')
# for key in model.wv.similar_by_word(seed, topn =10):
#     tem=getlive(key[0])
#     print(tem.subject+'\t'+str(tem.tags))
# # print(model.wv[seed])