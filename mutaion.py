from init import init
import numpy as np
import random

def mutaion(newPopulation : list, initValues : init):
    mask = np.zeros((initValues.n, initValues.l), dtype=int)
    
    for i in range(initValues.n):
        for j in range(initValues.l):
            if (random.random() <= initValues.pm):
                mask[i, j] = 1
                
    population = np.bitwise_xor(newPopulation, mask)
    return population