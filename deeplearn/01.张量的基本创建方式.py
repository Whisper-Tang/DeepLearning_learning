# 张量的创建方式
# 张量：
#   PyTorch框架属于最常用的深度学习框架，它提供了丰富的张量操作和神经网络模块。
#   ANN：人工神经网络; CNN：卷积神经网络; RNN：循环神经网络;
#   在底层处理数据时，都是使用  张量  来进行处理的。
#   张量 ==> 存储同一类型元素的容器， 且元素必须是数值类型。
# 张量的创建方式：
# torch.tensor() 根据指定的数据创建张量
# torch.Tensor() 根据指定的形状创建张量,也可创建指定数据类型的张量
# torch.IntTensor()         # 创建指定类型的张量
# torch.FloatTensor() 
# torch.BoolTensor() 
# torch.ByteTensor() 

# 导入PyTorch框架
import torch
import numpy as np

# 定义函数,演示：# torch.tensor() 根据指定的数据创建张量
def dm1():
    
    # 1.标量张量
    t1 = torch.tensor(100)
    print(f't1: {t1},\ntype: {type(t1)}')
    print('-'*30)
    
    # 2.二维表 张量
    data = [[100, 200, 300],[400, 500, 600]]
    t2 = torch.tensor(data)
    print(f't2: {t2},\ntype: {type(t2)}')
    print('-'*30)
   
    # 3.根据NumPy数组创建张量
    np_data = np.random.randint(0, 100, size=(2, 3))
    t3 = torch.tensor(np_data)
    print(f't3: {t3},\ntype: {type(t3)}')
    print('-'*30)


# 定义函数,演示：# torch.Tensor() 根据指定的形状创建张量,也可创建指定数据类型的张量
def dm2():
    # 4.根据指定的形状创建张量
    t4 = torch.zeros((2, 3))
    print(f't4: {t4},\ntype: {type(t4)}')
    print('-'*30)
# 定义函数,演示：# torch.IntTensor()         # 创建指定类型的张量
def dm3():
    # 5.创建指定类型的张量
    np_data = np.random.randint(0, 100, size=(2, 3))
    t5 = torch.FloatTensor(np_data)     # 类型不匹配，会自动转换，默认32位浮点数
    print(f't5: {t5},\ntype: {type(t5)}')
    print('-'*30)
# 测试函数
if __name__ == '__main__':
    dm3()
