from init import init
import numpy as np
import math


def fitEval(realValues : np.array, initValues : init):
    fit = []
    selectionProbability = []
    for i in range(initValues.n):
        x = realValues[i,:]
        fit.append((1+math.cos(2*math.pi*x[0]*x[1]))*math.exp(-(abs(x[0]))+abs(x[1]))/2)
    
    sumFit = sum(fit)
    for i in range(initValues.n):
        selectionProbability.append(fit[i]/sumFit)
        
    aveFit = sumFit/len(fit)
    maxFit = max(fit)
    maxLocation = fit.index(maxFit)
    optSol = realValues[maxLocation,:]
    
    return selectionProbability, fit, aveFit, maxFit, optSol
    