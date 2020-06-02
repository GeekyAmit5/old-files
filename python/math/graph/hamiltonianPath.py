def hamiltonian(x):
    global cycle, total
    if len(cycle) == n:
        print(cycle)
        total += 1
    else:
        for i in connections[x]:
            if i not in cycle:
                cycle.append(i)
                hamiltonian(i)
                cycle.pop()


n = 5
vertices = [x for x in range(n)]  # vertices
connections = [[0, 1], [1, 2, 4], [1, 3, 4],
               [2, 4], [1, 2, 3]]     # adjacency list
cycle = []
total = 0
for i in vertices:
    cycle.append(i)
    hamiltonian(i)
    cycle = []
print("Total =", total)
