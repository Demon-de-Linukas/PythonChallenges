from math import *
import os
import time
import matplotlib.pyplot as plt

import numpy as np
from fractions import Fraction
from decimal import Decimal
from decimal import getcontext
from sympy import *


def love(t):
    x=16*sin(t)**3
    y=13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
    return x,y

def get_heart():
    t=0
    xachse=[]
    yachse=[]
    xstart, ystart=love(t)
    xachse.append(xstart)
    yachse.append(ystart)
    t=0.2
    i=0
    while t< 50:
        x, y = love(t)
        i+=1
        if i==5:

            xachse.append(x)
            yachse.append(y)
            i=0
        #print(t)
        if x==xstart and y==ystart:
            break
        t+=0.2
    x_convert = np.asarray(xachse) * 0.05 + 1
    y_convert = np.asarray(yachse) * 0.05 + 1.2
    plt.plot(x_convert, y_convert)
    plt.show()
    return x_convert.tolist(),y_convert.tolist()


def get_position(xachse, zachse):
    sequence=[]
    for i in range(len(xachse)):
        sequence.append((xachse[i],2,zachse[i],0))
    return sequence


def timer(x):
    print('Start timer.')
    i=1
    while i<60*x:
        if i%60==0:
            print(str(i//60)+' min.')
        time.sleep(1)
        i+=1


timer(53)