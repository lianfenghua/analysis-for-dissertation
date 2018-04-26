# -*- coding: utf-8 -*-
'''能谱图。这里的设置顺序可以使LaTeX写的坐标轴名字具有正确的字体（Times New Roman），其他程序里的设置不行。'''
import numpy as np
import matplotlib.pyplot as plt

from data import data

#数据
Da = 0.0001
Re = 100
period = 6.04

#设置tex及字体
plt.rc('font', **{'family':'serif','serif':['times']})
plt.rc('text', usetex=True)


def plot_psd(df, variable):
    '''Plot Power spectral density (PSD) of the variable.
    df: DataFrame
    variable: A string
    '''
    t = df['Time']
    x = df[variable]
#    x = -2 * x        # Fy-->Cl, Fx-->Cd: Cl=-2*Fy, Cd=-2*Fx
#    variable = 'Cl'   # 
    mean = x.mean()
    
    fig, ax = plt.subplots(1, 2, figsize=(6, 2.6))

    #设置横纵坐标的名称以及对应字体格式
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size'  : 10.5,
            }

    #设置坐标刻度值的大小以及刻度值的字体
    plt.tick_params(labelsize=9)  
    labels = ax[0].get_xticklabels() + ax[0].get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    
    # variable-t
    ax[0].plot(t, x)
    ax[0].plot(t, [mean]*t.shape[-1])
#   ax[0].set_xlim(1,)
    ax[0].set_xlabel(r'$t$', fontdict=font)
#   ax[0].set_ylabel(r'${0}$'.format(variable), size='x-large')
    ax[0].set_ylabel(r'$V$', fontdict=font)
    
    # Amplitude-f
    n = t.shape[-1]                  # Number of data points   
    dt = 1e-3                        # Sampling period
    Fk = np.fft.fft(x)/n             # Fourier coefficients (divided by n)
    freq = np.fft.fftfreq(n, d=dt)   # Natural frequencies
    Fk = np.fft.fftshift(Fk)         # Shift zero freq to center
    freq = np.fft.fftshift(freq)     # Shift zero freq to center

    #设置坐标刻度值的大小以及刻度值的字体
    plt.tick_params(labelsize=9)  
    labels = ax[1].get_xticklabels() + ax[1].get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    
#   ax[1].psd(x, NFFT=npoints, Fs=1/dt)
    
    ax[1].plot(freq, np.absolute(Fk)**2)   # Plot spectral power
#    ax[1].plot(0, mean, 'o')
    ax[1].set_xlim(0, 1)
#    ax[1].set_ylim(0, 0.006)
    ax[1].set_xlabel(r'$f$', fontdict=font)
    ax[1].set_ylabel('Amplitude', fontdict=font)
    
    fig.tight_layout()
    # Set the figure path saved
    fig_name = 'psd/{0}_{1}_V.pdf'.format(Da, Re)
    plt.savefig(fig_name)
    plt.show()


if __name__ == "__main__":
    for i in range(1):
        cdcl = data(Da, Re, 'Point3', period=period).load_data()#.tail(100000)
        plot_psd(cdcl, 'V')
        
        