import math


def hamiltonian(x):
    global cycle, total, weight, bestWeight, bestRoute
    if len(cycle) == n+1:
        print(cycle)
        print("Weight :", weight, end="\n\n")
        if weight < bestWeight:
            bestWeight = weight
            bestRoute = cycle[:]
        total += 1
    else:
        for i in range(len(connections[x])):
            if connections[x][i] not in cycle or (len(cycle) == n and connections[x][i] not in cycle[1:]):
                cycle.append(connections[x][i])
                weight += weightList[x][i]
                hamiltonian(connections[x][i])
                cycle.pop()
                weight -= weightList[x][i]


n = 5
vertices = [x for x in range(n)]  # vertices
connections = [[1, 3, 4], [0, 2, 4], [1, 3], [0,
                                              2, 4], [0, 1, 3]]     # adjacency list
weightList = [[5, 2, 3], [5, 6, 1], [6, 2],
              [2, 2, 3], [3, 1, 3]]      # weightList
cycle = []
weight = 0
bestWeight = math.inf
bestRoute = None
total = 0
for i in vertices:
    cycle.append(i)
    hamiltonian(i)
    cycle = []
print("Total Path".ljust(15), total, sep=" : ")
print("Minimum Weight".ljust(15), bestWeight, sep=" : ")
print("Best Path".ljust(15), bestRoute, sep=" : ")
