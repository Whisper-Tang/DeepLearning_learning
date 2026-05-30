"""
创建全0_1_指定值的张量

函数：
    # 创建全0张量
    torch.zeros() 和 torch.zeros_like()

    # 创建全1张量
    torch.ones() 和 torch.ones_like()

    # 创建指定值的张量
    torch.full() 和 torch.full_like()

    # 创建对角线为1的张量
    torch.eye() 和 torch.eye_like()
掌握：
    zeros(),  full()
"""

# 导入
import torch

# t2 是一个二维张量，三行三列
t2 = torch.tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# 演示1：torch.zeros() 和 torch.zeros_like() # 创建全0张量


def dm1():
    t1 = torch.zeros((2, 3))
    print(f't1: {t1},\ntype: {type(t1)}')
    print('-'*30)

    # t3 --> 基于 t2 创建形状相同的全0张量
    t3 = torch.zeros_like(t2)
    print(f't3: {t3},\ntype: {type(t3)}')
    print('-'*30)

# 演示2：torch.ones() 和 torch.ones_like() # 创建全1张量


def dm2():
    t4 = torch.ones((2, 3))
    print(f't4: {t4},\ntype: {type(t4)}')
    print('-'*30)

    # t5 --> 基于 t2 创建形状相同的全1张量
    t5 = torch.ones_like(t2)
    print(f't5: {t5},\ntype: {type(t5)}')
    print('-'*30)

# 演示3：torch.full() 和 torch.full_like() # 创建全为指定值的张量
def dm3():
    t6 = torch.full((2, 3), fill_value=521)
    print(f't6: {t6},\ntype: {type(t6)}')
    print('-'*30)

    # t7 --> 基于 t2 创建形状相同的全为666的张量
    t7 = torch.full_like(t2, fill_value=666)
    print(f't7: {t7},\ntype: {type(t7)}')
    print('-'*30)


# 测试函数
if __name__ == '__main__':
    dm3()
