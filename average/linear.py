# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:29:38 2018

@author: user-lfh
"""
'''
[x1, u1, p1] = [1.6206399999999999,-0.007862397500000002,-1.1868749999999935]
[x2, u2, p2] = [1.65388,0.010014757182692307,-1.1736038461538492]

x0 = x1 - u1*(x2-x1)/(u2-u1)
p0 = p1 + (p2-p1)*(x0-x1)/(x2-x1)
'''

[theta1, p1] = [36.0,0.0435294117647]
[theta2, p2] = [37.125,-0.0083137254902]
theta0 = theta1 - p1*(theta2-theta1)/(p2-p1)

