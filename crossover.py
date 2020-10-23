from init import init
import numpy as np
import random

def crossover(initValues : init, matingPool : list):
    parentNum = np.random.permutation(initValues.n)
    newPopulation = np.zeros((initValues.n, initValues.l) , dtype=int)
    for j in range(0, initValues.n, 2):
        pointer1 = parentNum[j]
        pointer2 = parentNum[j+1]
        cutPoint = random.randint(1,initValues.l - 1)
        
        off1 = matingPool[pointer1, :]
        off2 = matingPool[pointer2, :]
        
        if (random.random() < initValues.pc):
            temp = off2
            off2[cutPoint:-1] = off1[cutPoint:-1]
            off1[cutPoint:-1] = temp[cutPoint:-1]
            
        newPopulation[j, :] = off1
        newPopulation[j+1, :] = off2
        
    return newPopulation
    #print(newPopulation)