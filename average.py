# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv

#参数
Da = 0.001
Re = 200
base = 630000
period1000 = 5300
step = np.arange(base+100, base+period1000, 100)


#读取文件并求和
variables = ['X', 'Y', 'U', 'V', 'Vort', 'P']
skip = np.array([0, 1, 6726, 6727, 20252, 20253])
dtype = {'X': float, 'Y': float, 'U': float, 'V': float, 'Vort': float, 'P': float}

filename = '../data/new/average/{0}_{1}/unpcy_{1}_time_{2}_flow.dat'.format(Da, Re, step[0])
flow = pd.read_csv(filename, sep='\s+',
                   quoting=csv.QUOTE_NONE,
                   skiprows=skip,
                   names=variables,
                   dtype=dtype)

for i in range(1, len(step)):
    filename = '../data/new/average/{0}_{1}/unpcy_{1}_time_{2}_flow.dat'.format(Da, Re, step[i])
    newflow = pd.read_csv(filename, sep='\s+',
                          quoting=csv.QUOTE_NONE,
                          skiprows=skip,
                          names=variables,
                          dtype=dtype)
    flow[['U', 'V', 'Vort', 'P']] += newflow[['U', 'V', 'Vort', 'P']]
#求平均
flow[['U', 'V', 'Vort', 'P']] /= len(step)
#压力系数转换
free_index = flow[(flow.X==-30) & (flow.Y==0)].index.tolist()[0]
free_pressure = flow.P.loc[free_index]
flow['P'] = (flow['P'] - free_pressure) * 2
'''
#保存到文件中
savename = "../analysis/averagefile/{}_{}_flow.dat".format(Da, Re)
flow.to_csv(savename, sep='\t', header=False, index=False)

#添加字符串
top = 'VARIABLES = "X", "Y", "U", "V", "Vort", "P"\n'
blk1 = 'ZONE T="BLK 1 "  I= 82, J=82, F=POINT\n'
blk2 = 'ZONE T="BLK 2 "  I= 322, J=42, F=POINT\n'
blk3 = 'ZONE T="BLK 3 "  I= 322, J=202, F=POINT\n'
string = [top, blk1, top, blk2, top, blk3]

fp = open(savename)
lines = []
for line in fp: # 内置的迭代器, 效率很高
    lines.append(line)
fp.close()

for i in range(6):
    lines.insert(skip[i], string[i]) # 在第二行插入
s = ''.join(lines)
fp = open(savename, 'w')
fp.write(s)
fp.close()
'''


#数据分为三块，分别处理
flow1 = flow.loc[0: 6723].reset_index(drop=True)
flow2 = flow.loc[6724: 20247].reset_index(drop=True)
flow3 = flow.loc[20248: 85291].reset_index(drop=True)
'''
#截取 y=0 处的值
#flow1
def center_for_square(M, N):
    'M x N'
    underbegin = int((M/2-1)*M); underend = underbegin + (M-1)
    overbegin = int((M/2)*M); overend = overbegin + (M-1)
    under = flow1.loc[underbegin: underend].reset_index(drop=True)
    over = flow1.loc[overbegin: overend].reset_index(drop=True)
    return (under + over)/2
M = 82; N = 82
center1 = center_for_square(M, N)
#flow2
def center_for_ring(flowname, M, N):
    'M x N'
    left_index = [i*M for i in range(N)]
    left = flowname.loc[left_index].reset_index(drop=True)
    right_under_index = [i*M + int(M/2-1) for i in range(N)]
    right_over_index = [i*M + int(M/2) for i in range(N)]
    right = (flowname.loc[right_under_index].reset_index(drop=True) + \
             flowname.loc[right_over_index].reset_index(drop=True) ) / 2
    return pd.concat([left, right])
M = 322; N = 42
center2 = center_for_ring(flow2, M, N)
#flow3
M = 322; N = 202
center3 = center_for_ring(flow3, M, N)
#合并
center = pd.concat([center1, center2, center3]).reset_index(drop=True)
center = center[['X', 'U', 'P']]
center = center.sort_values(by='X')
#保存到文件中
centername = "../analysis/averagefile/{}_{}_center.dat".format(Da, Re)
center.to_csv(centername, sep='\t', header=False, index=False)
'''

#截取圆上的值，只涉及flow2或flow3，取它们的平均值
#flow2
M = 322; N = 42
begin = 0; end = int(M/2-1)
surface2 = flow2.loc[begin: end].reset_index(drop=True)
#flow3
M = 322; N = 202
begin = (N-1) * M; end = begin + int(M/2-1)
surface3 = flow3.loc[begin: end].reset_index(drop=True)
#取平均值
surface = (surface2 + surface3) / 2
#将x，y两列换成角度
surface = surface[['X', 'U', 'V', 'Vort', 'P']]
surface.rename(columns={surface.columns[0]: "Theta"}, inplace=True)
surface['Theta'] = np.linspace(0, 180, 161)
#保存到文件中
surfacename = "../analysis/averagefile/{}_{}_surface.dat".format(Da, Re)
surface.to_csv(surfacename, sep='\t', header=False, index=False)




