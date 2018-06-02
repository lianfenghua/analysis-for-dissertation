# -*- coding: utf-8 -*-
'''平均升力系数和文献的对比'''
import matplotlib.pyplot as plt
import numpy as np
import itertools

import constants as c

# 读取数据
Da = 1e-05
Re = c.Re
Cl_amplitude = c.Cl_amplitude[0]
ref = np.loadtxt('ClAmplitude.txt')

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 15,
        }

# 画图
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# Plot new data
ax.plot(Re, Cl_amplitude, label=r'$Da={}$'.format(Da))

# Plot data from reference
ax.plot(ref[:,0], ref[:,1], 'd', markersize=4,
        label='Solid (Jeongyoung Park, 1998)')

# Plot solid data
""" Re = c.Re_solid
Cl_amplitude_solid = c.Cl_amplitude_solid
ax.plot(Re, Cl_amplitude_solid, marker=marker.next(), markersize=2,
        linewidth=1, linestyle=linestyle.next(),
        label='Solid')
 """

#ax.set_xlim(40, 280)
#ax.set_ylim(0, 0.3)
ax.set_xlabel(r'$Re$', fontdict=font)
ax.set_ylabel(r'$C_L^A$', fontdict=font)

plt.legend(prop=font)
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('validation_Cl2.pdf')
plt.show()

