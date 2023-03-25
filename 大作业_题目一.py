#1.请用数值方法求方程f(x)=x^2 - 8x + 6的根，精度取0.0001，标记为A、B；（25分）
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False

x0 = float(input('输入初始点x0：较大值\n'))
x1 = float(input('输入初始点x1：较小值\n'))
m = 1e-4 #0.0001迭代界限
# 函数
init_fun = lambda x: x ** 2 - 8 * x + 6
# 图像格式设置
plt.style.use('ggplot')
fig_1 = plt.figure(figsize=(8, 6))
plt.hlines(0, -1, x0, 'black')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('$f(x)=x^2 - 8x + 6$ 202208201122 仲文豪 题目一')
# 迭代法计算求解
def root(func=init_fun, x0=x0, x1=x1, theta=m):
    while True:
        x2 = x0 - func(x0) * (x1 - x0) / (func(x1) - func(x0))
        plt.vlines(x0, 0, init_fun(x0), 'green', '--')
        plt.scatter(x0, func(x0), c='black')
        if abs(func(x2)) < theta:
            return round(x2,4)
        x0 = x1
        x1 = x2
xi = root(init_fun, x0, x1, m)
print('此方程的其中一根的坐标为：' + '('+ str(xi)+ ','+ '0'+ ')')
# 绘制函数图像（函数区间默认暂定为（-1,10），步长为0.05）
x = []
if x0 > 0:
    x = np.arange(-1, x0, 0.05)
else:
    x = np.arange(x0, 10, 0.05)
y = init_fun(x)
plt.plot(x, y)
plt.show()


