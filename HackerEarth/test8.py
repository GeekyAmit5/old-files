def solve():
    q = [b]
    for i in range(k):
        x = len(q)
        for j in range(x):
            if 0 <= q[0] - c[i] <= l:
                q.append(q[0] - c[i])
            if 0 <= q[0] + c[i] <= l:
                q.append(q[0] + c[i])
            q.pop(0)
    ans = len(set(q))
    if ans:
        print(ans)
    else:
        print(-1)


l, k = map(int, input().split())
b = int(input())
c = list(map(int, input().split()))

solve()