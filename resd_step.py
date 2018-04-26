# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from data import data


Da = 0.0001
Re = 50
St = 0.11
period = 1/St
resd = data(Da, Re, 'resd', period=False, nperiods=5).load_data()

Iter = resd['Iter']
Step = Iter/30
#time = Step/1000

fig, ax = plt.subplots(figsize=(8,4))
ax.semilogy(Step, resd['Resor0'], label='Resor0')
ax.semilogy(Step, resd['Resor1'], label='Resor1')
ax.semilogy(Step, resd['Resor2'], label='Resor2')
ax.set_xlabel('Step')
ax.set_ylabel('Error')
#ax.set_xlim(3e5, 3e5+2)
#ax.set_ylim(-1e-3, 6e-3)
ax.legend()
plt.tight_layout()
fig_name = '../figs/{0}_{1}/resd.pdf'.format(Da, Re)
#plt.savefig(fig_name)
plt.show()

