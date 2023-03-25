#1.请用数值方法求方程f(x)=x^2 - 8x + 6的极值（最大或最小），精度取0.00001，标记为C点；（25分）
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文
plt.rcParams['axes.unicode_minus']=False #正常显示负号
#初始函数定义
def f(x):
    return x**2 -8*x + 6
#一次求导定义
def d_f_1(x):
    return 2*x - 8
#迭代梯度公式与下降精度
def d_f_2(f, x, delta=1e-5):
    return (f(x+delta) - f(x-delta)) / (2 * delta)

#参数设置
learning_rate = 0.1
max_loop = 70#下降次数
#梯度降点初值设定
x_init = 10.0
x = x_init
lr = 0.1
#第一个图的相关参数存储
draw_y_1=[]#存储过程下降值来存储数值
#梯度下降过程

for i in range(max_loop):
    d_f_x = d_f_2(f, x)
    x = x - learning_rate * d_f_x
    print("第",i+1,"次梯度下降,","下降后的 x = ",round(x,5))
    draw_y_1.append(x)
print("极小值点坐标"+"(",round(x,5),",",round(f(x),5),")")


#绘制函数图形和极值点
# 图像格式设置
plt.style.use('ggplot')
fig_1 = plt.figure(figsize=(8, 6))
#绘制子图01——x梯度下降过程值显示
draw_x_1 = np.array(np.arange((10/max_loop), 10+(10/max_loop),(10/max_loop)))
plt.subplot(1, 2, 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title('x梯度下降过程值显示 仲文豪 题目二')
plt.scatter(draw_x_1,draw_y_1,marker='v',color='b')

#绘制子图02——函数图像和所求极值点显示
plt.subplot(1,2,2)
xs = np.arange(-1, 10,0.05)
plt.plot(xs, f(xs))
plt.scatter(x,f(x),color='b')
plt.annotate(f'{round(x,5),round(f(x),5)}',xy=(x,f(x)),xytext=(round(x,5),round(f(x),5)),textcoords='offset points')
# 绘制两条正交直线
plt.axvline(x=[0.0],ls='--',color='g')
plt.axhline(y=[0.0],ls='--',color='g')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('$Q(x)=x^2 - 8x + 6$ 仲文豪 题目二')
plt.show()
