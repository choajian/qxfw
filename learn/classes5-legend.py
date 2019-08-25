import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
#set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 本节中我们将对图中的两条线绘制图例，首先我们设置两条线的类型等信息（蓝色实线与红色虚线).
l1,= plt.plot(x,y1,label='linear line')
l2,= plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--',label='square line')

# legend将要显示的信息来自于上面代码中的 label. 所以我们只需要简单写下一下代码, plt 就能自动的为我们添加图例.
# plt.legend(loc='upper right')

# best自适应
plt.legend(handles=[l1,l2],labels=['up','down'],loc='lower left')
plt.show()

