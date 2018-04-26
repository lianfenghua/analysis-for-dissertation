# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import itertools

import constants as c

# 读取数据
Da = c.Da
Re = c.Re
period = c.period
St = 1./np.array(period)
for i in range(len(St[0])):
    print('%.4f' % St[0][i])

#ref = np.loadtxt('St.txt')


# 画图
fig, ax = plt.subplots()
marker = itertools.cycle(('o', 's', '^'))
linestyle = itertools.cycle(('-', '-.', '--'))


for i in range(len(Da)):
    ax.plot(Re, St[i], marker=marker.next(), markersize=2,
            linewidth=1, linestyle=linestyle.next(),
            label=r'$Da$={}'.format(Da[i]))


# Plot data from reference
#ax.plot(ref[:,0], ref[:,1], 'd', markersize=4,
#        label='Solid from Measurement Williamson(1992)')


# Plot solid data
""" Re = c.Re_solid
period = c.period_solid
St = 1./np.array(period)
ax.plot(Re, St, marker=marker.next(), markersize=2,
        linewidth=1, linestyle=linestyle.next(),
        label='Solid')
 """

#ax.set_xlim(40, 280)
#ax.set_ylim(0, 0.3)
ax.set_xlabel(r'$Re$', fontsize=10.5)
ax.set_ylabel(r'$St$', fontsize=10.5)
plt.xticks(fontsize=10.5)
plt.yticks(fontsize=10.5)
plt.legend(fontsize=10.5)
ax.grid()
plt.legend()
fig.tight_layout()
plt.savefig('St_Re.pdf')
plt.show()

