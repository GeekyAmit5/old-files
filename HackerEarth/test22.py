l, k = map(int, input().split())
b = int(input())
c = list(map(int, input().split()))
q = [(b, 0)]
while q[0][1] != k:
    if 0 <= q[0][0]-c[q[0][1]] <= l and (q[0][0]-c[q[0][1]], q[0][1]+1) not in q:
        q.append((q[0][0]-c[q[0][1]], q[0][1]+1))
    if 0 <= q[0][0]+c[q[0][1]] <= l and (q[0][0]+c[q[0][1]], q[0][1]+1) not in q:
        q.append((q[0][0]+c[q[0][1]], q[0][1]+1))
    q.pop(0)
    if not q:
        print(-1)
        break
else:
    print(len(q))
