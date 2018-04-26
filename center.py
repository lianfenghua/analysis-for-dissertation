# -*- coding: utf-8 -*-
'''平均量沿中心线的变化'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

import constants as c

#参数
Da = 0.001
Re = [50, 70, 100, 120, 160, 200]

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 20.5,
        }

linestyle = itertools.cycle(('-', '--', '-.', ':', (0, (3, 5, 1, 5, 1, 5)), (0, (1, 1))))

'''
#u
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Re)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da, Re[i])
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])
	ax.plot(center['X'], center['U'],
			linestyle=linestyle.next(), linewidth=.8,
			label=r'$Re={}$'.format(Re[i]))
ax.plot(np.linspace(-30, 30, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-30, 30)
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$\overline{u}$', fontdict=font)

plt.legend()
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/u_x_{}.pdf'.format(Da))
plt.show()
'''

#放大u
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Re)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da, Re[i])
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])
	ax.plot(center['X'], center['U'],
			linestyle=linestyle.next(), linewidth=.8)
ax.plot(c.x0[Da], [0]*6, 'x')
ax.plot(np.linspace(-0.5, 8, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-0.5, 8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$\overline{u}$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/u_x_wake_{}.pdf'.format(Da))
plt.show()

'''
#Cp
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Re)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da, Re[i])
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])	
	ax.plot(center['X'], center['P'],
			linestyle=linestyle.next(), linewidth=.8)
ax.plot(np.linspace(-30, 30, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-30, 30)
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$C_p$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Cp_x_{}.pdf'.format(Da))
plt.show()
'''

#放大Cp
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Re)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da, Re[i])
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])	
	ax.plot(center['X'], center['P'],
			linestyle=linestyle.next(), linewidth=.8)
#	ax.plot(1.87338, -0.76099, 'kx')
ax.plot(c.x0[Da], c.p0[Da], 'x')
ax.plot(np.linspace(-0.5, 8, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-0.5, 8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$C_p$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Cp_x_wake_{}.pdf'.format(Da))
plt.show()

