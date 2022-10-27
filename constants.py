
import scipy.integrate as integrate
from equations import *
from simpson import simpson
from numpy import *
import numpy as np
import math
#Define constants that are used in project

#Neural network configuration paramaters
HIDDEN_NODES = 10
lamda = 1
LAYERS = 3
ALPHA = 0.5
#Tan-sigmoid function
def tansig(x):
  x = (x)
  eq = (e**(x)-e**(-x))/(e**(x)+e**(-x))
  return eq

def sig(x):
  x = (x)
  eq = 1/(1+e**(-x))
  return eq

#Leaku RELU
def lRelu(x):
  if x<0:
    return x/10
  else:
    return x

def integration(x, Phi):
  #eq = integrate.quad(lambda t: Phi(x-t)*(t**(ALPHA-1)), 0, x-A)[0]/sqrt(pi) + integrate.quad(lambda t: h(x, t)*Phi(t), 0, 1)[0]

  #eq = integrate.quad(lambda t: Phi(t)*(x-t)**(1-ALPHA)), 0, x)[0]*lamda/sqrt(pi)\
   #   + integrate.quad(lambda t: h(t)*(x-t)**(1-ALPHA)), 0, x)[0]/sqrt(pi)

  eq = integrate.quad(lambda t:(h(t)+lamda*Phi(t)) * (x - t) ** (ALPHA-1), 0, x)[0] /math.gamma(ALPHA)

  return eq 

