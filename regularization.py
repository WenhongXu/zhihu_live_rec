#基本信息的标准化，之后存入csv

from load_data import load_corpus,index_item
import pandas as pd 
import numpy as np
from functiontool.baseinfo import getlive
sentences,words,validatewords,user = load_corpus('corpus_all.txt',usertxt='dir.txt')
assert len(sentences)==len(user)
index2item,item2index,vocabulary=index_item(words)
vocabulary_size=len(vocabulary)
future_batch= 5
print(vocabulary_size)
print(user[:30])
# sentences : 序列中的元素为live原始id
# words:  按热度排序的live列表,带有词频率，所以是个元组
# validatewords:  选取最后的几个作为抹去的对象，这些对象作为验证集使用
# user: 和sentences索引对应的用户id列表
# vocabulary： 按词频排序的列表

#已经获取了所有的索引信息，至此，数据集索引加载完成,且没有划分
print('所有内容报名完成，下面开始加载数据')

#下面加载基本信息

def get_user_base(user):
    from sqlalchemy import create_engine
    base_engine = create_engine("mysql+pymysql://root:19971012@127.0.0.1:3306/zhihu", max_overflow=5)
    print('读取40万用户开始')
    df = pd.read_sql('user',base_engine)
    df.set_index(["id"], inplace=True)
    print('读取完成')
    df = df.loc[tuple(user),]
    # print(df[:3])
    # df1 = df['gender']
    df_count = ['answer_count', 'articles_count', 'columns_count', 'favorited_count',
    'follower_count', 'following_count','hosted_live_count',
    'live_count', 'pins_count',
    'question_count', 'thanked_count', 'voteup_count']
    for i in df_count:
        d = df[i].astype('float')
        # print(d)
        d= (d - d.min()) / (d.max()-d.min())
        df2 = df.drop(i, axis=1)
        df[i] = d
    # df2 = df2.apply(lambda x: (x - np.mean(x)) / np.std(x))
    # df = pd.concat([df1,df2])
    return df[['answer_count', 'articles_count', 'columns_count', 'favorited_count',
    'follower_count', 'following_count','hosted_live_count','live_count', 'pins_count',
    'question_count', 'thanked_count', 'voteup_count','gender']]

def get_live_base(lives):
    print('开始加载live信息')
    livesss = []
    for i in lives:
        if i in ['843515877629501440','1087372616938983424']:
            live_dict = {'id': i, 'attachment_count': 0,
                'audio_duration': 0, 'reply_message_count': 0,
                'speaker_audio_message_count': 0,
                'speaker_message_count': 0,'fee': 0,
                'liked_num': 0, 'people_count': 0,
                'review_count': 0, 'review_score': 0
                            }
            print(live_dict)
            livesss.append(live_dict)
            continue
        ob = getlive(i)
        print(i)
        live_dict = {'id': ob.id, 'attachment_count': ob.attachment_count,
                'audio_duration': ob.audio_duration, 'reply_message_count': ob.reply_message_count,
                'speaker_audio_message_count': ob.speaker_audio_message_count,
                'speaker_message_count': ob.speaker_message_count,'fee': ob.fee,
                'liked_num': ob.liked_num, 'people_count': ob.people_count,
                'review_count': ob.review_count, 'review_score': ob.review_score
                            }
        print(live_dict)
        livesss.append(live_dict)
    print('加载基本完成')
    df = pd.DataFrame(livesss)
    df.set_index(["id"], inplace=True)
    # print(df)
    for i in df.columns:
        d = df[i].astype('float')
        # print(d)
        d= (d - d.min()) / (d.max()-d.min())
        # print(d)
        df = df.drop(i, axis=1)
        df[i] = d
    print(df)
    return df


# user_base = get_user_base(user)
# user_base.to_csv('user_base_all.csv')

live_base= get_live_base(vocabulary)
live_base.to_csv('live_base_all.csv')
