from init import init
from chromeDecode import chromeDecode
from fitEval import fitEval
from rouletteWheel import rouletteWheel
from crossover import crossover
from mutaion import mutaion
import matplotlib.pyplot as plt


obj = init()

bestSoFar = []
finalSol = None
averageFitness = []

print("Calculating ... ")

for it in range(obj.iteration):
    realValues = chromeDecode(obj)
    selectionProbability, fit, aveFit, maxFit, optSol = fitEval(realValues, obj)
    
    if (it == 0):
        bestSoFar.append(maxFit)
        finalSol = optSol
    elif (maxFit > bestSoFar[it-1]):
        bestSoFar.append(maxFit)
        finalSol = optSol
    else:
        bestSoFar.append(bestSoFar[it-1])
        
    averageFitness.append(aveFit)
    
    matinPool = rouletteWheel(obj, selectionProbability)
    newPopulation = crossover(obj, matinPool)
    obj.population = mutaion(newPopulation, obj)
    
    
print(finalSol)
plt.plot(bestSoFar, label="Best So Far")
plt.plot(averageFitness, label="Average Fitness")
plt.title("result = " + str(finalSol))
plt.xlabel('Itration')
plt.legend()
plt.show()