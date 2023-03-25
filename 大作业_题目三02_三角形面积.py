import 大作业_题目三01_函数封装 as ABC
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #正常显示中文
plt.rcParams['axes.unicode_minus']=False #正常显示负号
import numpy as np
# 输入三角形三个顶点的坐标，计算三角形的面积
class Trangle:
    #定义三个点的类属性
    def Point1(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def Point2(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def Point3(self, x3, y3):
        self.x3 = x3
        self.y3 = y3

    #求三条边的距离
    def s1(self):
        self.a = ((self.x2 - self .x1)**2 + (self.y2 - self.y1) ** 2)**(1 / 2)
        print("第一条边长为", round(self.a,5))
    def s2(self):
        self.b = ((self.x3 - self .x2)**2 + (self.y3 - self.y2) ** 2)**(1 / 2)
        print("第二条边长为:", round(self.b,5))
    def s3(self):
        self.c = ((self.x3 - self .x1)**2 + (self.y3 - self.y1) ** 2)**(1 / 2)
        print("第三条边长为:", round(self.c,5))

    #通过海伦公式用三条边求面积
    def Area(self):
        s = (self.a + self.b + self.c) / 2
        area = pow((s * (s - self.a) * (s - self.b) * (s - self.c)), 0.5)
        print("三角形的面积：%0.5f" % (area))

if __name__ == '__main__':
    ABC.root_A()
    ABC.root_B()
    A_X, A_Y = ABC.Get_A()
    B_X, B_Y = ABC.Get_B()
    C_X, C_Y = ABC.root_C()
    # 检验封装函数结果
    print('A坐标为：' + '(' + str(A_X) + ',' + str(A_Y) + ')')
    print('B坐标为：' + '(' + str(B_X) + ',' + str(B_Y) + ')')
    print('C坐标为：' + '(' + str(C_X) + ',' + str(C_Y) + ')')
    # 调用函数，构建ABC三角形，并求面积
    a = Trangle()
    a.Point1(A_X, A_Y)
    a.Point2(B_X, B_Y)
    a.Point3(C_X, C_Y)
    a.s1()
    a.s2()
    a.s3()
    a.Area()
    #绘制图形
    xs = np.arange(-1, 10,0.05)
    plt.plot(xs, ABC.f(xs))
    plt.scatter(A_X,A_Y,color='r')
    plt.annotate(f'{A_X,A_Y}',xy=(A_X,A_Y),xytext=(A_X,A_Y),textcoords='offset points')
    plt.scatter(B_X,B_Y,color='y')
    plt.annotate(f'{B_X,B_Y}',xy=(B_X,B_Y),xytext=(B_X,B_Y),textcoords='offset points')
    plt.scatter(C_X,C_Y,color='b')
    plt.annotate(f'{C_X,C_Y}',xy=(C_X,C_Y),xytext=(C_X,C_Y),textcoords='offset points')
    X=[[A_X,B_X,C_X,A_X]]
    Y=[[A_Y,B_Y,C_Y,A_Y]]
    for i in range(len(X)):
        plt.plot(X[i],Y[i],linestyle='--',color='gray')
    # 绘制两条正交直线
    plt.axvline(x=[0.0],ls='--',color='g')
    plt.axhline(y=[0.0],ls='--',color='g')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('$Q(x)=x^2 - 8x + 6$ 仲文豪 题目三')
    plt.show()