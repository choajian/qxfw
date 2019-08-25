import matplotlib.pyplot as plt
import numpy as np

# 使用np.linspace定义x：范围是(-3,3);个数是50.
# 仿真一维数据组(x ,y1)表示曲线1. 仿真一维数据组(x ,y2)表示曲线2.
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

# 使用plt.figure定义一个图像窗口. 使用plt.plot画(x ,y2)曲线.
# 使用plt.plot画(x ,y1)曲线，曲线的颜色属性(color)为红色;
# 曲线的宽度(linewidth)为1.0；曲线的类型(linestyle)为虚线.
# 使用plt.xlim设置x坐标轴范围：(-1, 2)； 使用plt.ylim设置y坐标轴范围：(-2, 3)；
plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth='1.0',linestyle='--')
plt.xlim((-1,2))
plt.ylim((-2,3))

# 使用np.linspace定义范围以及个数：范围是(-1,2);个数是5.
# 使用plt.xticks设置x轴刻度：范围是(-1,2);个数是5.
# 使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’].
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],['$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])

# 使用plt.gca获取当前坐标轴信息.
# 使用.spines设置边框：右侧边框；使用.set_color设置边框颜色：默认白色；
# 使用.spines设置边框：上边框；使用.set_color设置边框颜色：默认白色；
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#plt.show()

# 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom.
# （所有位置：top，bottom，both，default，none）

ax.xaxis.set_ticks_position('bottom')

# 使用.spines设置边框：x轴；使用.set_position设置边框位置：y=0的位置；
# （位置所有属性：outward，axes，data）

ax.spines['bottom'].set_position(('data', 0))

# 使用.yaxis.set_ticks_position设置y坐标刻度数字或名称的位置：left.
# （所有位置：left，right，both，default，none）
ax.yaxis.set_ticks_position('left')

# 使用.spines设置边框：y轴；使用.set_position设置边框位置：x=0的位置；
# （位置所有属性：outward，axes，data） 使用plt.show显示图像.
ax.spines['left'].set_position(('data',0))

plt.show()