# -*- coding: utf-8 -*-
'''平均量沿中心线的变化，多个达西数在同一个图中'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

#参数
Da = [1e-05, 0.0001, 0.001]
Re = 100

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 20.5,
        }

linestyle = itertools.cycle(('-', '--', '-.'))


#u
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Da)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da[i], Re)
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])
	ax.plot(center['X'], center['U'],
			linestyle=linestyle.next(), linewidth=.8,
			label=r'$Da={}$'.format(Da[i]))
ax.plot(np.linspace(-30, 30, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-30, 30)
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$\overline{u}$', fontdict=font)

plt.legend()
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/u_x_Re{}.pdf'.format(Re))
plt.show()


#放大u
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Da)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da[i], Re)
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])
	ax.plot(center['X'], center['U'],
			linestyle=linestyle.next(), linewidth=.8)
#	ax.plot(1.87338, 0, 'kx')
ax.plot(np.linspace(-0.5, 8, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-0.5, 8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$\overline{u}$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/u_x_wake_Re{}.pdf'.format(Re))
plt.show()


#Cp
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Da)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da[i], Re)
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])	
	ax.plot(center['X'], center['P'],
			linestyle=linestyle.next(), linewidth=.8)
ax.plot(np.linspace(-30, 30, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-30, 30)
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$C_p$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Cp_x_Re{}.pdf'.format(Re))
plt.show()


#放大Cp
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Da)):
	centername = "../analysis/averagefile/{}_{}_center.dat".format(Da[i], Re)
	center = pd.read_csv(centername, sep='\t', names=['X', 'U', 'P'])	
	ax.plot(center['X'], center['P'],
			linestyle=linestyle.next(), linewidth=.8)
#	ax.plot(1.87338, -0.76099, 'kx')
ax.plot(np.linspace(-0.5, 8, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(-0.5, 8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xlabel(r'$x$', fontdict=font)
ax.set_ylabel(r'$C_p$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Cp_x_wake_Re{}.pdf'.format(Re))
plt.show()

