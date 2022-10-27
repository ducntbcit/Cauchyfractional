from numpy import *
import numpy as np
import scipy.integrate as integrate
import math
#Define equations of the examples in the project file

NUMBER = 2 #No. of examples in project

#Right-side equation (Свободная функция с правой стороны)
def right_eq(x):
    #eq = 2*sqrt(x-1)/sqrt(pi)+np.e**x + 1/2

    eq = 0
    return eq

#Analytical solution
def analytic(x):

    # eq = x
    #eq = x**2
    eq = math.log(x)
    return eq

def h(x):
    №eq = 0
    # eq = 2*sqrt(x)/sqrt(pi) - x
    #eq = (1.76522*x**(1.25))-x**2
    eq = math.log(4*x)/sqrt(pi*x)
    return eq
