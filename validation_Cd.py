# -*- coding: utf-8 -*-
'''平均阻力系数和文献的对比'''
import matplotlib.pyplot as plt
import numpy as np
import itertools

from data import data
import constants as c

# 读取数据
Da = 1e-05
Re = c.Re
period = c.period[0]
ref = np.loadtxt('meanDrag.txt')

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 15,
        }

color = ['b', 'g', 'r']
marker = ['o', 's', 'D']
linestyle = ['--', '-.', '-']

fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]


# 画图
meanCd = np.zeros_like(period) # 平均阻力
for j in range(len(Re)):
    cdcl = data(Da, Re[j], 'cdcl', period[j], nperiods=1).load_data()
    meanCd[j] = -2*cdcl['Fxc'].mean()
ax.plot(Re, meanCd, color=color[0],
        marker=marker[0], markersize=4,
        linestyle=linestyle[0], linewidth=1,
        label=r'$Da={}$'.format(Da))

# Plot solid data
Da = 0
Re = c.Re_solid
period = c.period_solid
solidCd = np.zeros_like(period)
for j in range(len(Re)):
    cdcl = data(Da, Re[j], 'cdcl', period[j], nperiods=1).load_data()
    solidCd[j] = 2*cdcl['Fx'].mean()
ax.plot(Re, solidCd, color=color[1],
        marker=marker[1], markersize=4,
        linestyle=linestyle[1], linewidth=1,
        label=r'Solid, $Da=0$')

# Plot data from reference
ax.plot(ref[:,0], ref[:,1], color=color[2],
        marker=marker[2], markersize=4,
        linestyle=linestyle[2], linewidth=1,
        label='Solid (Rajani, 2008)')


# Show figures
ax.set_xlabel(r'$Re$', fontdict=font)
ax.set_ylabel(r'$C_D$', fontdict=font)

plt.legend(prop=font)
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('validation_Cd2.pdf')
plt.show()

