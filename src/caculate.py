import math
import os
import numpy as np

from fractions import Fraction
from decimal import Decimal
from decimal import getcontext
from sympy import *
from numpy import *
from numpy.linalg import inv

from sympy.abc import x, y

# import sympy




def science(n):
    print("%e" % n)

"------------------------------------------------------"

# Constant definition
h = 6.626e-34  # Planke Constant
k = 1.38e-23  # Boltzman Constant
m0 = 9.10938e-31  # Elektronen Mass
eq = 1.60217648740e-19  # Elementarladung
ev = 1.6021765314e-19  # ev to Joel
E0 = 8.854187817e-12  # Dielektrizitaetkonstante

pi = math.pi
e = math.e

def sqrt(n):
    return float(math.sqrt(n))


def oneDFunc(p1,p2):
    n1=np.array([[p1[0],1],[p2[0],1]])
    n2=np.array([p1[1],p2[1]])
    lsg=np.dot(inv(n1),n2)
    print(lsg)
    return lsg


def ln(n):
    return float(math.log(n))


def dTf(self):
    lenth = int(len(str(self)))
    srrr = str(self)
    indexOfDot = int(str(self).index('.'))
    numberString = srrr[indexOfDot:lenth]
    numberString = '0' + numberString
    try:
        f = float(numberString)
    except ValueError:
        print('invalid %s' % (numberString))
    r = lenth - indexOfDot + 2
    numerator = int(f * (10 ** r))
    denominator = int(10 ** r)
    result = Fraction(numerator, denominator)
    return str(result)


def getDerivative(f, n, time):
    result = diff(f, n, time)
    return result


def getIntegrate(f, n):
    result = str(integrate(f, n))
    result += '+C'
    return result


def oneDgetY(a, b, x):
    print(a*x+b)
    return a*x+b

parm=oneDFunc([15,0.25],[115,4.75])
a=parm[0]
b=parm[1]

oneDgetY(a, b, 90)
oneDgetY(a, b, 97.5)
oneDgetY(a, b, 100)


# dt=np.array([15,12,3,17,5,8])
# ma=6*756-60**2
# print(np.sum(dt[:]*dt[:]))
# print(ma)

#############################################################
#        while True:
#           print('>>')
#           dynamic = input('New Calculation: ')
#           if dynamic != 'cls':
#                   result=eval(dynamic)
#                   print(str(result))
#           else:
#                   break
#        os.system('cls')








