# -*- coding: utf-8 -*-
'''平均量沿圆柱表面的变化'''
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


#Cp
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Da)):
    surfacename = "../analysis/averagefile/{}_{}_surface.dat".format(Da[i], Re)
    surface = pd.read_csv(surfacename, sep='\t', names=['Theta', 'U', 'V', 'Vort', 'P'])
    ax.plot(surface['Theta'], surface['P'],
            linestyle=linestyle.next(), linewidth=.8,
            label=r'$Da={}$'.format(Da[i]))
ax.plot(np.linspace(0, 180, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(0, 180)
ax.set_xticks([0, 30, 60, 90, 120, 150, 180])
ax.set_xlabel(r'$\theta[^\circ]$', fontdict=font)
ax.set_ylabel(r'$C_p$', fontdict=font)

plt.legend()
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Cp_theta_Re{}.pdf'.format(Re))
plt.show()

'''
#Vort
fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=18)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#画图
for i in range(len(Re)):
    surfacename = "../analysis/averagefile/{}_{}_surface.dat".format(Da, Re[i])
    surface = pd.read_csv(surfacename, sep='\t', names=['X', 'Y', 'U', 'V', 'Vort', 'P'])
    ax.plot(angle, surface['Vort'],
            linestyle=linestyle.next(), linewidth=.8)
ax.plot(np.linspace(0, 180, 2), [0]*2, 'k-', linewidth=.2)

ax.set_xlim(0, 180)
ax.set_xticks([0, 30, 60, 90, 120, 150, 180])
ax.set_xlabel(r'$\theta[^\circ]$', fontdict=font)
ax.set_ylabel(r'$\frac{\omega}{\sqrt{Re}}$', fontdict=font)

ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('average/Vort_theta_{}.pdf'.format(Da))
plt.show()
'''
