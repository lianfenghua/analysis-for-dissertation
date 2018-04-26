# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from data import data

#参数
Da = 0.01
Re = 180

def change_over_time(df, variable):
    '''Plot the variation of the variable.
    df: DataFrame
    variable: A string
    '''
    t = df['Time']
    x = df[variable]
    x = -2 * x                 # for Cl

    #设置tex及字体
    plt.rc('font', **{'family':'serif','serif':['times']})
    plt.rc('text', usetex=True)

    #设置横纵坐标的名称以及对应字体格式
    font = {'family': 'Times New Roman',
            'weight': 'normal',
           'size'  : 20.5,
           }

    fig, ax = plt.subplots(figsize=(6, 3.5))

    #设置坐标刻度值的大小以及刻度值的字体
    plt.tick_params(labelsize=15)  
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    #画图
    ax.plot(t, x)

#    ax.set_xlim(100,)
    ax.set_ylim(-0.0001, 0.0001)
    ax.set_xlabel(r'$t$', fontdict=font)
    ax.set_ylabel(r'$C_L$', fontdict=font)

    #输出
    fig.tight_layout()
    plt.savefig('Cl/{0}_{1}.pdf'.format(Da, Re))
    plt.show()


if __name__ == "__main__":
    # Cl-t
    for i in range(1):
        cdcl = data(Da, Re, 'cdcl').load_data()
        change_over_time(cdcl, 'Fyc')

