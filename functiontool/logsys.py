from functiontool.templib import temp_stupid
import datetime
import json
#这是一个日志系统，我觉得python的log用作试验记录不太好用，就写了个简单的
class recorder:
    def __init__(self):
        '''
        you have to record the content below
        the parameter you specified
        the outline of your experiment
        the index of effect e.g. SSE
        '''
        self.da = datetime.datetime.now()
        self.sum = temp_stupid('./log/readme.csv')
        self.fi = temp_stupid('./log/'+self.da.strftime('%y-%m-%d-%H-%M-%S')+'.json')
        self.para = {}
    
    def login(self,**kargs):
        self.para.update(kargs)
    
    def wri(self,outline:str):
        self.para['outline'] = outline
        self.para['starttime'] = self.da.strftime('%y-%m-%d-%H-%M-%S')
        self.para['endtime'] = (datetime.datetime.now()-self.da).seconds
        self.para['status'] = 'success'
        self.sum.save([self.da.strftime('%y-%m-%d-%H-%M-%S')+','+outline])
        self.fi.update([json.dumps(self.para,ensure_ascii=False)])
    def err(self,outline,message):
        self.sum.save([self.da.strftime('%y-%m-%d-%H-%M-%S')+','+outline+'#'+','+'normal'])
        self.fi.update([json.dumps({'status':'failed','outline':outline,'msg':message},ensure_ascii=False)])

class printer:
    '''
    print record of experiment
    '''
    ...

# if __name__=='__main__':
#     re = recorder()
#     re.login(name='meta',method = 'stupid')
#     re.wri('这是一次小小的实验，用于测试实验记录模块的作用')


