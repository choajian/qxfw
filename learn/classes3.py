import matplotlib.pyplot as plt
import numpy as np

# 使用np.linspace定义x：范围是(-3,3);个数是50.
# 仿真一维数据组(x ,y1)表示曲线1. 仿真一维数据组(x ,y2)表示曲线2.
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

# 使用plt.figure定义一个图像窗口：编号为3；大小为(8, 5).
# 使用plt.plot画(x ,y2)曲线. 使用plt.plot画(x ,y1)曲线，
# 曲线的颜色属性(color)为红色;曲线的宽度(linewidth)为1.0；
# 曲线的类型(linestyle)为虚线. 使用plt.show显示图像.
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0, linestyle='--')

# 使用plt.xlim设置x坐标轴范围：(-1, 2)； 使用plt.ylim设置y坐标轴范围：(-2, 3)；
# 使用plt.xlabel设置x坐标轴名称：’I am x’； 使用plt.ylabel设置y坐标轴名称：’I am y’；

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
#plt.show()

# 使用np.linspace定义范围以及个数：范围是(-1,2);个数是5.
# 使用print打印出新定义的范围. 使用plt.xticks设置x轴刻度：范围是(-1,2);个数是5.
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)

# 使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]. 使用plt.show显示图像.
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()