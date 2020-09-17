t = int(input())
ans = []
for i in range(t):
    g, p = map(int, input().split())
    n = int(input())
    q1, q2 = [], []
    for i in range(n):
        temp = input()
        a, b = map(int, temp.split())
        q1.append(a)
        q2.append(b)
    m = min(g, p)
    M = max(g, p)
    mQ = min(sum(q1), sum(q2))
    MQ = max(sum(q1), sum(q2))
    ans.append(mQ*M+m*MQ)
for i in ans:
    print(i)
