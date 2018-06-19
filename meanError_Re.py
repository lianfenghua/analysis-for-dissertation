# -*- coding: utf-8 -*-
'''平均误差随雷诺数的变化'''
import matplotlib.pyplot as plt
import numpy as np
import itertools

from data import data
import constants as c


Da = c.Da[0:3]
Re = c.Re
period = c.period[0:3]


fig, ax = plt.subplots(3, 1, sharex=True, figsize=(8, 12))
#fig, ax = plt.subplots()
marker = itertools.cycle(('o', 's', '^'))
linestyle = itertools.cycle(('-', '-.', '--'))

meanResd0 = np.zeros_like(period)
meanResd1 = np.zeros_like(period)
meanResd2 = np.zeros_like(period)
for i in range(len(Da)):
    for j in range(len(Re)):
        resd = data(Da[i], Re[j], 'resd', period[i][j], nperiods=5).load_data()
        meanResd0[i][j] = resd['Resor0'].mean()
        meanResd1[i][j] = resd['Resor1'].mean()
        meanResd2[i][j] = resd['Resor2'].mean()
    # Plot the data
    mk = marker.next()
    ls = linestyle.next()
    ax[0].plot(Re, meanResd0[i], marker=mk,
            linestyle=ls,
            label=r'$Da$={}'.format(Da[i]))
    ax[1].plot(Re, meanResd1[i], marker=mk,
            linestyle=ls,
            label=r'$Da$={}'.format(Da[i]))
    ax[2].plot(Re, meanResd2[i], marker=mk,
            linestyle=ls,
            label=r'$Da$={}'.format(Da[i]))

ax[2].set_xlabel(r'$Re$')
ax[0].set_ylabel('Resor0')
ax[1].set_ylabel('Resor1')
ax[2].set_ylabel('Resor2')
ax[0].legend()
fig.tight_layout()
plt.savefig('meanError_Re.pdf')
plt.show()

