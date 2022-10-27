from numpy import *
from data import *
from neural_network import *
from minimize import min
from plot import * 
from table import * 
import timeit
#Start minimizing with given initial weights
start = timeit.default_timer()
weights = min(W0)
#st rtweights = loadtxt("weights2.txt", delimiter=",")

stop = timeit.default_timer()
time = stop - start
second = round(time % 60)
hours = round(time / 3600)
minute = round((time%3600) / 60)

print(f"Minimizing time: {hours}h-{minute}m-{second}s")

#Process neural network with minimized weights
print(f"New neural network has error: {error(weights)}")
Y = []
Z = []

for x in X:
    Y.append(NN(weights, x))
    Z.append(analytic(x))

NN_plot(Y, Z)#Draw neural network plot
Err_plot(Y, Z)#Draw error plot
createTable(Y, Z)



