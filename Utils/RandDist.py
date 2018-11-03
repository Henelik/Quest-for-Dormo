from math import tan, pi
from random import uniform, randrange
from numba import jit

@jit(cache=True)
def tanDist(min, max):
    #return a random number between the min and max with a
    #Pareto-like distribution weighted towards the median
    x = uniform(0.0, 1.0)
    w = (1+(tan(pi*(x-0.5)/2))**3)/2
    return(w*(max-min)+min)

@jit(cache=True)
def cubeDist(min, max):
    #A faster version of tanDist with less weight towards the median
    x = uniform(0.0, 1.0)
    w = (((x-0.5)**3)*4)+0.5
    return(w*(max-min)+min)

@jit(cache=True)
def quinDist(min, max):
    #A steeper version of cubeDist (more weight towards median)
    x = uniform(0.0, 1.0)
    w = (((x-0.5)**5)*16)+0.5
    return(w*(max-min)+min)

@jit(cache=True)
def discreteRand(d):
    #Takes a dictionary of values (as keys) with weight values,
    #and returns a random value with that weight
    total = 0
    for i in d:
        total += d[i]
    index = randrange(1, total + 1)
    for i in d:
        if index > d[i]:
            index -= d[i]
        else:
            return i

@jit(cache=True)
def boolRand(chance): # Weighted boolean chance.  The higher the chance, the more likely the result will be True
    x = uniform(0.0, 1.0)
    if x < chance:
        return(True)
    else:
        return(False)
