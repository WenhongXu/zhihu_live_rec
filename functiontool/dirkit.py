import os
from functiontool.templib import temp_stupid
def getdir(path,fil=None,pre='.txt',to='dir.txt',display = False):
    '''
    该函数用户获得某一目录下的所有文件名
    path: 目录
    fil: a list 其中的内容会被过滤掉，相当于git中的.gitignore
    pre: 如果需要去除文件名的类型，默认去掉文件名之后的'.txt'
    to: 把结果输出到一个文件
    display： 是否要在运行过程中打印每个结果

    '''
    filePath = path
    lis=os.listdir(filePath)
    if pre:
        lis = [x.replace(pre,'') for x in lis]
    if fil:
        lis = list(filter((lambda x:True if x not in fil else False),lis))
    temp_stupid(to).update(lis)
    if display:
        print(lis)
    return lis

if __name__ =='__main__':
    getdir('./',['constant'],'.py')