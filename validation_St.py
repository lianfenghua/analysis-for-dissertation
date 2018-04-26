# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import itertools

import constants as c

# 读取数据
Da = c.Da[0]
Re = c.Re
period = c.period[0]
St = 1./np.array(period)

ref = np.loadtxt('St.txt')

# 画图
fig, ax = plt.subplots(figsize=(4.8,3.6))
marker = itertools.cycle(('o', 's', '^'))
linestyle = itertools.cycle(('-', '-.', '--'))

# Plot new data
for i in reversed(range(1)):
    ax.plot(Re, St,
            linestyle=linestyle.next(),
            label=r'$Da$={}'.format(Da))
# marker=marker.next(),markersize=2,linewidth=1, 
#ax.set_xlim(40, 280)
#ax.set_ylim(0, 0.3)

# Plot data from reference
ax.plot(ref[:,0], ref[:,1], 'd', markersize=4,
        label='Solid (Williamson, 1992)')

# Plot solid data
""" Re = c.Re_solid
period = c.period_solid
St = 1./np.array(period)
ax.plot(Re, St, marker=marker.next(), markersize=2,
        linewidth=1, linestyle=linestyle.next(),
        label='Solid')
 """

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=9)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 10.5,
        }
ax.set_xlabel(r'$Re$', fontdict=font)
ax.set_ylabel(r'$St$', fontdict=font)

#输出
plt.legend(prop=font)
fig.tight_layout()
plt.savefig('validation_St.pdf')
plt.show()

