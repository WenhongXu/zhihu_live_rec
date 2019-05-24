def generatecorpus():
    from functiontool.getrelation import getrelation
    from functiontool.templib import temp_stupid
    sample = temp_stupid('./sample/dir.txt').read()
    from functiontool.kit import tranverse
    k=set()
    def a(i):
        p=getrelation(i)
        for x in p:
            k.add(x)
    tranverse(sample,a)
    return k
    # temp_stupid('corpus.txt').update(k)
# se = list(generatecorpus())
from gensim.models import Word2Vec
from functiontool.baseinfo import getlive
model = Word2Vec.load("item2vec_sg1_hs0_size32_window5_50k.model")
seed = '833695646706978816'
seeddd=getlive(seed)
print('种子live----'+seeddd.subject+'     '+str(seeddd.tags))
print('\n')
for key in model.wv.similar_by_word(seed, topn =6):
    tem=getlive(key[0])
    print(tem.subject+'\t'+str(tem.tags))
    print('===============')



