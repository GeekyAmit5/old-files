from itertools import permutations as perm
import math
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

b = list(perm(a))
print(b)
mx = -math.inf
mn = -mx
for i in b:
    ans = 0
    for j in range(0, n, 2):
        ans += (i[j] ^ i[j+1])
    if ans > mx:
        mx = ans
    if ans < mn:
        mn = ans
print(mn, mx)
