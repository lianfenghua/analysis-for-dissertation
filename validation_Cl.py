# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import itertools

import constants as c


# 读取数据
Da = c.Da_new
Re = c.Re_new
Cl_amplitude = c.Cl_amplitude

ref = np.loadtxt('ClAmplitude.txt')


# 画图
fig, ax = plt.subplots()
marker = itertools.cycle(('o', 's', '^'))
linestyle = itertools.cycle(('-', '-.', '--'))

# Plot new data
for i in reversed(range(len(Da))):
    ax.plot(Re, Cl_amplitude[i], marker=marker.next(), markersize=2,
            linewidth=1, linestyle=linestyle.next(),
            label=r'$Da$={} new'.format(Da[i]))

# Plot data from reference
ax.plot(ref[:,0], ref[:,1], 'd', markersize=4,
        label='Solid from Jeongyoung Park(1998)')

# Plot solid data
""" Re = c.Re_solid
Cl_amplitude_solid = c.Cl_amplitude_solid
ax.plot(Re, Cl_amplitude_solid, marker=marker.next(), markersize=2,
        linewidth=1, linestyle=linestyle.next(),
        label='Solid')
 """

#ax.set_xlim(40, 280)
#ax.set_ylim(0, 0.3)
ax.set_xlabel(r'$Re$')
ax.set_ylabel(r'The amplitude of lift coefficient')
plt.legend()
fig.tight_layout()
plt.savefig('validation_Cl.pdf')
plt.show()

