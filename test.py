#测试我的模型
from keras import models
from keras import layers
import keras as K
import numpy as np
from keras import backend as K
data=np.load('test_doubel_atten_150.npz')
posi_data=data['posi_data']
nega_data=data['nega_data']
pp = len(posi_data[0])
num = len(posi_data)
print(posi_data)
model=models.load_model('double_atten.h5')
hitsum = 0
ndcgsum = 0

for i in range(num):
    pre = model.predict(np.array(posi_data[i]).reshape((1,pp)))
    # o = model.layers[6].output
    # print(o)
    true = pre[0][0]
    n = nega_data[i]
    pre = model.predict(n)
    # o = model.layers[6].output
    # print(o)
    false = pre[0]
    nn=0
    for i in false:
        if i>true:
            nn+=1
        else:
            print(str(i)+'<'+str(true))
    print(nn)
    rank_target = nn+1
    ndcg = 1/np.log2(rank_target+1)
    if nn<1:
        hitsum+=1
    if nn<5:
        ndcgsum+=ndcg
print(hitsum/num)
print(ndcgsum/num)

    

