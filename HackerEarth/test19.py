from itertools import permutations as p


def sum(a):
    s = abs(a[-1] - a[0])
    for i in range(len(a)-1):
        s += abs(a[i]-a[i+1])
    return s


n = int(input())
a = list(map(int, input().split()))
b = list(p(a))
m = -1
for i in b:
    ans = sum(i)
    if ans > m:
        m = ans
print(m)
