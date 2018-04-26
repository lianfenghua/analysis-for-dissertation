# -*- coding: utf-8 -*-
'''平均阻力系数'''
import matplotlib.pyplot as plt
import numpy as np
import itertools

from data import data
import constants as c

# 读取数据
#ref = np.loadtxt('meanDrag.txt')
Da = c.Da
Re = c.Re
period = c.period

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)

#设置横纵坐标的名称以及对应字体格式
font = {'family': 'Times New Roman',
        'weight': 'normal',
        'size'  : 10.5,
        }

#marker = itertools.cycle(('o', '^', 's'))
#linestyle = itertools.cycle(('-', '--', '-.'))
color = ['b', 'g', 'r']
marker = ['^', 'v']
linestyle = ['-', '--', '-.']

fig, ax = plt.subplots(dpi=200)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=10.5)  
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 画图
meanCd = np.zeros_like(period) # 平均阻力
meanCdp = np.zeros_like(period) # 压差阻力
meanCdf = np.zeros_like(period) # 摩擦阻力
for i in range(len(Da)):
    for j in range(len(Re)):
        cdcl = data(Da[i], Re[j], 'cdcl', period[i][j], nperiods=1).load_data()
        meanCd[i][j] = -2*cdcl['Fxc'].mean()
        meanCdp[i][j] = -2*cdcl['Fpx'].mean()
        meanCdf[i][j] = meanCd[i][j] - meanCdp[i][j]
    # print
    print('Da =', Da[i])
    for k in range(len(meanCd[i])):
        print('%.4f' % meanCd[i][k])
    print(' ')
    for k in range(len(meanCdp[i])):
        print('%.4f' % meanCdp[i][k])
    print(' ')
    for k in range(len(meanCdf[i])):
        print('%.4f' % meanCdf[i][k])
    # Plot the data
#    ax.plot(Re, meanCd[i], marker=marker.next(),
#            label=r'$Da={}, C_d$'.format(Da[i]))
    ax.plot(Re, meanCdp[i], color=color[i],
            marker=marker[0], markersize=3,
            linestyle=linestyle[i], linewidth=1,
            label=r'$Da={}, C_{}$'.format(Da[i], 'Dp'))
    ax.plot(Re, meanCdf[i], color=color[i],
            marker=marker[1], markersize=3,
            linestyle=linestyle[i], linewidth=1,
            label=r'$Da={}, C_{}$'.format(Da[i], 'Df'))

# Plot data from reference
#ax.plot(ref[:,0], ref[:,1], 'D-', label='Solid from Rajani(2008)')


# Plot solid data
""" Da = 0
Re = c.Re_solid
period = c.period_solid
solidCd = np.zeros_like(period)
for j in range(len(Re)):
    cdcl = data(Da, Re[j], 'cdcl', period[j], nperiods=1).load_data()
    solidCd[j] = 2*cdcl['Fx'].mean()
ax.plot(Re, solidCd, marker=marker.next(), linestyle='--',
        label='Solid')
 """

# Show figures
ax.set_xlabel(r'$Re$', fontdict=font)
ax.set_ylabel(r'$C_D$', fontdict=font)

plt.legend()
ax.grid(linestyle=':', linewidth=.2)
fig.tight_layout()
plt.savefig('meanCdpf_Re.pdf')
plt.show()

