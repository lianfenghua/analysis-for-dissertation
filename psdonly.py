# -*- coding: utf-8 -*-
"""能谱图"""
import numpy as np
import matplotlib.pyplot as plt

from data import data
import constants as c

#数据
Da = c.Da
Re = [c.Re[1], c.Re[5], c.Re[8], c.Re[11]]
period = [[c.period[0][1], c.period[0][5], c.period[0][8], c.period[0][11]],
          [c.period[1][1], c.period[1][5], c.period[1][8], c.period[1][11]],
          [c.period[2][1], c.period[2][5], c.period[2][8], c.period[2][11]]]
#print 'Da = ', Da
#print 'Re = ', Re

fig, ax = plt.subplots(4, 3, sharex='all', sharey='all', figsize=(6, 8.6))#, figsize=(9,4)

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)


def plot_psd(df, variable, i, j):
    '''Plot Power spectral density (PSD) of the variable.
    df: DataFrame
    variable: A string
    '''
    t = df['Time']
    x = df[variable]
#    x = -2 * x        # Fy-->Cl, Fx-->Cd: Cl=-2*Fy, Cd=-2*Fx
#    variable = 'Cl'   # 
#    mean = x.mean()
    
#    fig, ax = plt.subplots(3, 4, sharex='all', sharey='all')#, figsize=(9,4)
    
    # variable-t
#    ax[0].plot(t, x)
#    ax[0].plot(t, [mean]*t.shape[-1])
#    ax[0].set_xlim(1,)
#    ax[0].set_xlabel(r'$t$')
#    ax[0].set_ylabel(r'${0}$'.format(variable), size='x-large')
#    ax[0].set_ylabel(r'$C_L$')
    
    # Amplitude-f
    n = t.shape[-1]                  # Number of data points   
    dt = 1e-3                        # Sampling period
    Fk = np.fft.fft(x)/n             # Fourier coefficients (divided by n)
    freq = np.fft.fftfreq(n, d=dt)   # Natural frequencies
    Fk = np.fft.fftshift(Fk)         # Shift zero freq to center
    freq = np.fft.fftshift(freq)     # Shift zero freq to center
    
#    ax[1].psd(x, NFFT=n, Fs=1/dt)    # psd()
#    ax[i, j].magnitude_spectrum(x, Fs=1/dt)
    
    ax[i, j].plot(freq, np.absolute(Fk)**2)   # Plot spectral power
#    ax[1].plot(0, mean, 'o')
    ax[i, j].set_xlim(0, 1)
    ax[i, j].set_ylim(0, 0.2)
#    ax[1].set_xlabel(r'$f$')
#    ax[1].set_ylabel(r'Amplitude')

    #设置坐标刻度值的大小以及刻度值的字体
    plt.tick_params(labelsize=9)  
    labels = ax[i, j].get_xticklabels() + ax[i, j].get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    #设置横纵坐标的名称以及对应字体格式
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size'  : 10.5,
            }
    if j==0: ax[i, j].set_ylabel('Magnitude', fontdict=font)
    if i==3: ax[i, j].set_xlabel('Frequency', fontdict=font)
    

if __name__ == "__main__":
    for i in range(len(Da)):
        for j in range(len(Re)):
            print "Da =", Da[i]
            print "Re =", Re[j]
            cdcl = data(Da[i], Re[j], 'Point3', period=period[i][j]).load_data()#.tail(100000)
            plot_psd(cdcl, 'V', len(Da)-j, i)
    
    # 添加文字
    ax[0, 0].text(0.5, 1, r'$Da=0.00001$',
                  horizontalalignment='center',
                  verticalalignment='bottom',
                  transform=ax[0, 0].transAxes)
    ax[0, 1].text(0.5, 1, r'$Da=0.0001$',
                  horizontalalignment='center',
                  verticalalignment='bottom',
                  transform=ax[0, 1].transAxes)
    ax[0, 2].text(0.5, 1, r'$Da=0.001$',
                  horizontalalignment='center',
                  verticalalignment='bottom',
                  transform=ax[0, 2].transAxes)
    ax[0, 2].text(1.02, 0.5, r'$Re=200$',
                  horizontalalignment='left',
                  verticalalignment='center',
                  rotation='vertical',
                  transform=ax[0, 2].transAxes)
    ax[1, 2].text(1.02, 0.5, r'$Re=140$',
                  horizontalalignment='left',
                  verticalalignment='center',
                  rotation='vertical',
                  transform=ax[1, 2].transAxes)
    ax[2, 2].text(1.02, 0.5, r'$Re=90$',
                  horizontalalignment='left',
                  verticalalignment='center',
                  rotation='vertical',
                  transform=ax[2, 2].transAxes)
    ax[3, 2].text(1.02, 0.5, r'$Re=50$',
                  horizontalalignment='left',
                  verticalalignment='center',
                  rotation='vertical',
                  transform=ax[3, 2].transAxes)

    fig.tight_layout()
    # Set the figure path saved
    fig_name = 'psd/V.pdf'
    plt.savefig(fig_name)
    plt.show()
    