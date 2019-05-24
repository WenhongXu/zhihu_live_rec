#过滤器管理器

from pybloom_live import ScalableBloomFilter
from functiontool.templib import temp_stupid
import shelve

class bloom:
    '''
    过滤器管理器
    过滤器用于去重，在数据量很大的时候，使用时生成一个过滤器，通过数据库或文件向其中注入已经处理的对象是很慢的
    于是想到，对于可能中断的任务，将一次执行获得的过滤器保存下来，下一次读取就能接着使用
    这个类就实现这样的功能
    '''
    def __init__(self):
        '''
        初始化，打开shelve数据库
        '''
        self.list = {}
        self.db = shelve.open('bloom')
    def get_from_shelve(self,name):
        '''
        从shelve数据库中获得过滤器对象
        name: 过滤器的名字
        '''
        try:
            pc = self.db[name]
        except:
            pc = ScalableBloomFilter(100000000,0.001)
        self.list[name]=pc
        return pc
    def gettemp(self):
        '''
        临时获取一个过滤器，该过滤器不会保存
        '''
        return ScalableBloomFilter(100000000, 0.001)
    def create_from_file(self,filename):
        '''
        从文件中获得一个过滤器，同样，不会保存
        '''
        what = ScalableBloomFilter(100000000,0.001)
        t=temp_stupid(filename)
        for i in t.read():
            what.add(i)
        return what
    def login(self,name,filter):
        '''
        如果想要保存新的过滤器，使用该函数
        name: 为要保存的过滤器指定一个名字
        filter: 传入过滤器对象
        '''
        self.list[name]=filter

    def save(self):
        '''
        如果需要保存过滤器，以方便下一次使用，使用该函数
        该函数将保存一切从shelve中获得的过滤器
        如果你想一个一个的保存，使用login函数
        '''
        for i in self.list.keys():
            self.db[i] = self.list[i]
    def close(self):
        '''
        过滤管理器需要显式关闭，在代码最后记得关闭
        主要是数据库的关闭操作
        '''
        self.db.close()



