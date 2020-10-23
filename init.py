import numpy as np

class init:
    n = 50 #number of chroms
    pc = .9 #cross over
    pm = .005 #mutation
    iteration = 100
    m = 2 #number of variables
    bs = [10, 10] #lenght of every gene chrome

    l = 0 #lenght of chrome
    for item in bs:
        l = l + item

    lo = [-4, -1.5] #The lower limit of the function
    hi = [2, 1] #High limit function
    population = np.random.randint(2,size=(n, l))