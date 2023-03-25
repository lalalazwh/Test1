# 初始函数定义
def f(x):
    return x ** 2 - 8 * x + 6


'''方程根求解——求A和B点坐标'''
m = 1e-4  # 0.0001迭代界限
'''A点坐标'''
x0_A = float(input('输入求A点初始点x0：较大值（建议输入：4）\n'))
x1_A = float(input('输入求A点初始点x1：较小值（建议输入：0）\n'))
def root_A(func=f, x0=x0_A, x1=x1_A, theta=m):
    while True:
        x2 = x0 - func(x0) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < theta:
            return round(x2, 4)
        x0 = x1
        x1 = x2
xi = root_A(f, x0_A, x1_A, m)


x0_B = float(input('输入求B点初始点x0：较大值（建议输入：10）\n'))
x1_B = float(input('输入求B点初始点x1：较小值（建议输入：4）\n'))
'''B点坐标'''
def root_B(func=f, x0=x0_B, x1=x1_B, theta=m):
    while True:
        x2 = x0 - func(x0) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < theta:
            return round(x2, 4)
        x0 = x1
        x1 = x2
xj = root_B(f, x0_B, x1_B, m)

'''最优解设计——求C点坐标'''
# 迭代梯度公式与下降精度
def d_f_2(f, x, delta=1e-5):
    return (f(x + delta) - f(x - delta)) / (2 * delta)
# 参数设置
learning_rate = 0.1
max_loop = 70  # 下降次数
# 梯度降点初值设定
x_C_init = 10
lr = 0.1
def root_C(fun2=d_f_2):
    x0=x_C_init
    for i in range(max_loop):
        d_f_x = fun2(f, x0)
        x0 = x0 - learning_rate * d_f_x
    return round(x0, 5),round(f(x0), 5)
def Get_A():
    return xi,0
def Get_B():
    return xj,0