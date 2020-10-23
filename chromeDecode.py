import numpy as np
from init import init
from functions import binArrayToInt

def chromeDecode(initValus:init):
    realValue = np.zeros((initValus.n, initValus.m), dtype=float)
    for i in range(initValus.n):
        row = initValus.population[i, :]
        sumation = 0
        for j in range(initValus.m):
            if (j == 0):
                sumation = initValus.bs[j]
                #print(row[0:sumation])
                temp = binArrayToInt(row[0:sumation])
                normal = temp / ((2**initValus.bs[j]) - 1)
                real = initValus.lo[j] + ((initValus.hi[j] - initValus.lo[j])* normal)
                realValue[i, j] = real
                # realValue[i, j] = np.packbits(row[0:sumation])
            else :
                #print(row[sumation:sumation + initValus.bs[j]])
                temp = binArrayToInt(row[sumation:sumation + initValus.bs[j]])
                normal = temp / ((2**initValus.bs[j]) - 1) 
                real = initValus.lo[j] + ((initValus.hi[j] - initValus.lo[j])* normal)
                realValue[i, j] = real
                sumation = sumation + initValus.bs[j]
    
    return realValue
