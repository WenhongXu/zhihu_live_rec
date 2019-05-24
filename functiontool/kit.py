import pandas as pd
import datetime
import math
import os

def dis_percent(li,ele):
    print('{:.2}%'.format((li.index(ele)+1)/len(li)*100))

def distinct(li):
    s=pd.Series(li).drop_duplicates()
    return list(s)

def tranverse(li,func,display=True):
    '''
    对li中的每个元素执行func操作
    这个函数是为了大进行遍历操作时，有时候耗时太长
    可以打印但是不知道啥时候结束
    这个函数可以告诉你遍历了百分之多少，还需要多长时间
    这样，就不那么焦虑对不对？
    '''
    
    li = list(li)
    le = len(li)
    if display:
        start = datetime.datetime.now()
    for i in range(le):
        func(li[i])
        if display:
            os.system('cls')
            have = (datetime.datetime.now()-start).seconds
            if have<0.1:
                continue
            speed = (i+1)/have
            need = (le-i-1)/speed
            print('{:.4}%'.format(100*i/le))
            print('还需要 {0}时{1}分{2}秒'.format(math.floor(need/3600),math.floor(need%3600/60),int(need%3600%60)))



if __name__=='__main__':
    print(distinct([1,2,2,2,3]))
