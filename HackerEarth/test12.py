
s = [i for i in input().split() if i.startswith('#')]

counts = {'#Sajid': 3, '#Amit': 3, '#Aman': 3,
          '#Salman': 4, '#Ritesh': 2, '#Arvish': 2}

j = 5
while j > 0:
    m = max(set(counts.values()))
    p = [k for k, v in counts.items() if v == m]
    p.sort()
    p = p[:j]
    j -= len(p)
    for i in p:
        print(i)
        counts.pop(i)
