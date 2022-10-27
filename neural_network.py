from numpy import *
from constants import *
from data import X, W0
from equations import *
def NN(W, x):

    b1 = W[0:HIDDEN_NODES]
    w1 = W[HIDDEN_NODES:HIDDEN_NODES*2]
    w2 = W[HIDDEN_NODES*2:HIDDEN_NODES*3]
    b2 = W[HIDDEN_NODES*3]
    z1 = []
    for i in range(0, len(w1)):
        temp = x*w1[i]+b1[i]
        z1.append(tansig(temp))
    a2 = b2
    for i in range(0, len(w2)):
        a2 += z1[i]*w2[i]
    N = tansig(a2)
    return N

def error(W):
    sum = 0
    for x in X:
        part = (NN(W, x) - integration(x, lambda t: NN(W, t)) - right_eq(x))**2
        sum += part
    return sum/len(X)
