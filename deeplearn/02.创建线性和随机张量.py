"""
演示PyTorch中如何创建 线性 和 随机张量

函数：
    
    # 创建线性张量
        torch.arange()
        torch.linspace()
    
    # 初始化随机种子  
        torch.random.initial_seed()  
        torch.random.manual_seed()    
    
    # 创建随机浮点类型张量
        torch.rand()
        torch.randn()

    # 创建随机整数类型张量
        torch.randint(low, high, size=())

掌握：
    arange(), linspace(), manual_seed(), randint();
    
"""
# 导入PyTorch框架
import torch
# 1.定义函数演示：创建线性张量


def dm1():
    # 1.1 创建指定范围的线性张量
    t1 = torch.arange(1, 15, 2)
    print(f't1: {t1},\ntype: {type(t1)}')
    print('-'*30)

    # 1.2 创建指定范围的线性张量 --> 等差数列
    t2 = torch.linspace(1, 10, 5)
    print(f't2: {t2},\ntype: {type(t2)}')
    print('-'*30)

# 2.定义函数演示：创建随机张量


def dm2():
    # step1：初始化随机种子
    # torch.initial_seed() # 采用当前系统时间戳作为随机种子
    torch.manual_seed(366)  # 设置随机种子为366，确保每次运行生成的随机数相同

    # step2：创建随机张量

    # 2.1 均匀分布随机张量
    t3 = torch.rand(size=(2, 3))
    print(f't3: {t3},\ntype: {type(t3)}')
    print('-'*30)

    # 2.2 正态分布随机张量
    t4 = torch.randn(size=(2, 3))
    print(f't4: {t4},\ntype: {type(t4)}')
    print('-'*30)

    # 2.3 创建指定范围的随机整数类型张量
    t5 = torch.randint(low=0, high=100, size=(2, 3))
    print(f't5: {t5},\ntype: {type(t5)}')
    print('-'*30)


# 3.测试函数
if __name__ == '__main__':
    dm2()
