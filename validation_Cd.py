# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import itertools

from data import data
import constants as c


# 读取数据
Da = c.Da_new
Re = c.Re_new
period = c.period_new

ref = np.loadtxt('meanDrag.txt')


# 画图
fig, ax = plt.subplots()
marker = itertools.cycle(('o', 's', '^'))
linestyle = itertools.cycle(('-', '-.', '--'))

# Plot new data
meanCd = np.zeros_like(period)
for i in reversed(range(len(Da))):
    for j in range(len(Re)):
        cdcl = data(Da[i], Re[j], 'cdcl', period[i][j], nperiods=1, new=True).load_data()
        meanCd[i][j] = -2*cdcl['Fxc'].mean()
    ax.plot(Re, meanCd[i], marker=marker.next(), linestyle='--',
            label=r'$Da$={} new'.format(Da[i]))

# Plot data from reference
ax.plot(ref[:,0], ref[:,1], 'D-', label='Solid from Rajani(2008)')

# Plot solid data
Da = 0
Re = c.Re_solid
period = c.period_solid
solidCd = np.zeros_like(period)
for j in range(len(Re)):
    cdcl = data(Da, Re[j], 'cdcl', period[j], nperiods=1).load_data()
    solidCd[j] = 2*cdcl['Fx'].mean()
ax.plot(Re, solidCd, marker=marker.next(), linestyle='--',
        label='Solid')


# Show figures
ax.set_xlabel(r'$Re$')
ax.set_ylabel('Mean drag coefficient')
plt.legend()
fig.tight_layout()
plt.savefig('validation_Cd.pdf')
plt.show()

