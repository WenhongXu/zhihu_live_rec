我写的有点多，函数函数之间的依赖关系有点复杂
简要说明一下

Airbnb在KDD2018的论文我想浮现来着
但是在tensorflow里手工实现时，出现了问题
简单来讲log(1-pn)由于学习率问题，反向传播过头了，负类的概率pn变成了1，log(1-1)=inf
后面采用了NCE函数完成了这个问题的解答
相关使用可以参照word2vec_basic.py，该文件来自tensorflow官方示例

尽管解决了，后面调学习率我也觉得很麻烦
所以直接用了gensim自然语言处理包，把live id当作单词处理了，得到了向量    word2vec.py
但是后来为了获取距离某一live最远的live，还是计算了距离举证     distance.py

数据基本信息存在数据库中，通过regularization.py变成了向user_base.csv这样的结果，读取采用pandas

购买关系数据的基本存储方式在gooduser/和goodlive/有示例

以data_for_double_开头的文件都是用来构造数据集的，文件名后面跟了_test的是测试集构造，没跟的是训练集构造
构造好的数据集会保存为npz/npy格式，这是numpy把数组存为二进制文件的格式
所以实现一次加载数据，多次在模型中使用，只要使用np.load('xxx.npz')

my_rec_model.py是我的模型，test.py是我模型的测试代码

log文件夹是我自己写的一个小小的试验记录“系统”（实际上就是一个python class）产生的
代码中出现recorder()是在使用这个试验记录"系统"，学姐可以不用管

load_data.py 是加载数据用的函数库

sample文件夹和负采样没关系！其中的文件保存了一些用户，这些用户有特征，在文件名中体现，为了方便取得特定的数据

最后推荐下自己写的functiontool工具包，我觉得还不错哈哈，但有些功能可能pandas之类的有实现，我懒得学，觉得简单就自己写了