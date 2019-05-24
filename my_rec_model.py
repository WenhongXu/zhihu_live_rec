#这就是我的模型

from keras import models
from keras import layers
import keras as K
import numpy as np
from keras import backend as K

data=np.load('for_doubel_atten_no_side.npz')
posi_data=data['posi_data']
nega_data=data['nega_data']
num = len(nega_data)
pp=len(posi_data[0])
trainnum = int(num*0.8)
posi_data=posi_data[:trainnum]
nega_data=nega_data[:trainnum]
x=np.concatenate((posi_data,nega_data))
dimension = len(posi_data)
y_p = np.ones(trainnum,dtype=np.int32)
y_n = np.zeros(trainnum,dtype=np.int32)
y = np.concatenate((y_p,y_n))
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(128,activation='relu',input_shape=(pp,)))
    model.add(layers.Dense(64,activation='relu'))
    model.add(layers.Dense(32,activation='relu'))
    model.add(layers.Dense(16,activation='relu'))
    model.add(layers.Dense(8,activation='relu'))
    model.add(layers.Dense(4,activation='relu'))
    # model.add(layers.Dense(2,activation='relu'))
    model.add(layers.Dense(1,activation='sigmoid'))
    model.compile(optimizer='adam',# 还可以通过optimizer = optimizers.RMSprop(lr=0.001)来为优化器指定参数
                loss='binary_crossentropy', # 等价于loss = losses.binary_crossentropy
                metrics=['accuracy']) # 等价于metrics = [metircs.binary_accuracy]
    return model
model = build_model()
model.fit(x,y,epochs=10,batch_size=512,shuffle=True,validation_split=0.1)
model.save('double_atten_no_side.h5')#保存模型
# data=np.load('test_doubel_atten_no_side_200.npz')
# posi_data=data['posi_data']
# nega_data=data['nega_data']
# pp = len(posi_data[0])
# num = len(posi_data)
# print(posi_data)
# # model=models.load_model('double_aver.h5')
# hitsum = 0
# ndcgsum = 0

# for i in range(num):
#     pre = model.predict(np.array(posi_data[i]).reshape((1,pp)))
#     # o = model.layers[6].output
#     # print(o)
#     true = pre[0][0]
#     n = nega_data[i]
#     pre = model.predict(n)
#     # o = model.layers[6].output
#     # print(o)
#     false = pre[0]
#     nn=0
#     for i in false:
#         if i>true:
#             nn+=1
#         else:
#             print(str(i)+'<'+str(true))
#     print(nn)
#     rank_target = nn+1
#     ndcg = 1/np.log2(rank_target+1)
#     if nn<1:
#         hitsum+=1
#     if nn<5:
#         ndcgsum+=ndcg
# print(hitsum/num)
# print(ndcgsum/num)

    
# # model=models.load_model('double.h5')
# # scores = model.evaluate(x,y,batch_size=512)
# # print(scores[1]*100)