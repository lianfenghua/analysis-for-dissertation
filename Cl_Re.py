# -*- coding: utf-8 -*-
'''平均升力系数'''
import matplotlib.pyplot as plt
import numpy as np
import itertools

from data import data
import constants as c

# 读取数据
Da = c.Da
Re = c.Re
period = c.period

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 15,
        }

#marker = itertools.cycle(('o', '^', 's'))
#linestyle = itertools.cycle(('-', '--', '-.'))
color = ['b', 'g', 'r', 'c']
marker = 'o'
marker = ['o', '^', 'v']
linestyle = ['-', '--', '-.', ':']

fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=15)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 画图
rmsCl = np.zeros_like(period) # 均方根升力
rmsClp = np.zeros_like(period) # 压差升力
rmsClf = np.zeros_like(period) # 摩擦升力
for i in range(len(Da)):
    for j in range(len(Re)):
        cdcl = data(Da[i], Re[j], 'cdcl', period[i][j], nperiods=1).load_data()
        rmsCl[i][j] = np.sqrt(((2*cdcl['Fyc'])**2).mean())
        rmsClp[i][j] = np.sqrt(((2*cdcl['Fpy'])**2).mean())
        rmsClf[i][j] = np.sqrt(((2*(cdcl['Fyc']-cdcl['Fpy']))**2).mean())
    # print
    print('Da =', Da[i])
    for k in range(len(rmsCl[i])):
        print('%.4f' % rmsCl[i][k])
    print(' ')
    # for k in range(len(rmsClp[i])):
    #     print('%.4f' % rmsClp[i][k])
    # print(' ')
    # for k in range(len(rmsClf[i])):
    #     print('%.4f' % rmsClf[i][k])
    # print(' ')
    # Plot the data
    ax.plot(Re, rmsCl[i], color=color[i],
            marker=marker[0], markersize=3,
    	    linestyle=linestyle[i], linewidth=1,
        	label=r"$Da={},\,$".format(Da[i])+r"$C_{L'}$")
    ax.plot(Re, rmsClp[i], color=color[i],
            marker=marker[1], markersize=3,
    	    linestyle=linestyle[i], linewidth=1,
        	label=r"$Da={},\,$".format(Da[i])+r"$C_{L'p}$")
    ax.plot(Re, rmsClf[i], color=color[i],
            marker=marker[2], markersize=3,
    	    linestyle=linestyle[i], linewidth=1,
        	label=r"$Da={},\,$".format(Da[i])+r"$C_{L'f}$")

# Show figures
ax.set_xlabel(r'$Re$', fontdict=font)
ax.set_ylabel(r"$C_{L'}$", fontdict=font)

plt.legend()
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('Clpf_Reaaa.pdf')
plt.show()

