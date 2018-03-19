import itertools
counter =0
solutions = []

def pathCounter(gridSize):
    path = []
    counter = 0
    for i in range(0,gridSize):
        path.append(0)
        path.append(1)
    print path
    for i in itertools.permutations(path,gridSize*2):
        if i not in solutions:
            print i
            solutions.append(i)
            counter=counter+1
    return  counter

n = pathCounter(2)
print n
