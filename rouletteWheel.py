from init import init
import random
import numpy as np


def rouletteWheel(initValues : init, selectionProbability : list):
    cdf = []
    cdf.append(selectionProbability[0])
    for i in range(1, initValues.n):
        cdf.append(cdf[i-1]+selectionProbability[i])
    
    matinPool =  np.zeros((initValues.n, initValues.l), dtype=int)  
    for i in range(initValues.n):
        q = random.random()
        for j in range(initValues.n):
            if (q <= cdf[j]):
                matinPool[i, :] = initValues.population[j , :]
                break
            
    return matinPool