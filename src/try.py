import math
import os

from fractions import Fraction
from decimal import Decimal
from decimal import getcontext
from sympy import *


class CaculateFunc:
    # Constant definition
    h = 6.626e-34  # Planke Constant
    k = 1.38e-23  # Boltzman Constant
    m0 = 9.10938e-31  # Elektronen Mass
    eq = 1.60217648740e-19  # Elementarladung
    ev = 1.6021765314e-19  # ev to Joel
    E0 = 8.854187817e-12  # Dielektrizitaetkonstante

    pi = math.pi
    e = math.e

    def science(self,n):
        print("%e" % n)

    def sqrt(self,n):
        return float(math.sqrt(n))

    def ln(self,n):
        return float(math.log(n))

    def decimal_to_fraction(self,func):
        lenth = int(len(str(func)))
        srrr = str(func)
        ##            print (srrr)
        ##            print (lenth)
        indexOfDot = int(str(func).index('.'))
        ##            print (indexOfDot)
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

    def getDerivative(self,f, n):
        var = Symbol(n)
        result = diff(f, var)
        return result

    def getIntegrate(self,f, n):
        var = Symbol(n)
        result = str(integrate(f, var))
        result += '+C'
        return result

    #############################################################
    while True:
        print('>>')
        dynamic = input('New Calculation: ')
        if dynamic != 'cls':
            result = eval(dynamic)
            print(str(result))
        else:
            break
    os.system('cls')








