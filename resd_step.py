# -*- coding: utf-8 -*-
'''误差'''
import matplotlib.pyplot as plt

from data import data

Da = 0.0001
Re = 45
period = 9.03

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 15,
        }

fig, ax = plt.subplots(figsize=(8,4))

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

resd = data(Da, Re, 'resd', period=False, nperiods=5).load_data()

Iter = resd['Iter']
Step = Iter/30
#time = Step/1000

ax.plot(Step, resd['Resor0'], label='Resor0',
            linestyle='-')
ax.plot(Step, resd['Resor1'], label='Resor1',
            linestyle='--')
ax.plot(Step, resd['Resor2'], label='Resor2',
            linestyle='-.')
ax.set_xlabel('Step', fontdict=font)
ax.set_ylabel('Error', fontdict=font)
#ax.set_xlim(3e5, 3e5+2)
ax.set_ylim(-1e-3, 4e-3)
ax.legend()
ax.grid(linestyle=':', linewidth=.2)
plt.tight_layout()
fig_name = 'resd/resd_{0}_{1}new.pdf'.format(Da, Re)
plt.savefig(fig_name)
plt.show()

