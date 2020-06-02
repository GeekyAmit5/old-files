# decimal into n-ary


import math


def n_ary(n, b):
    ans = 0
    for i in range(round(math.log(n, b)), -1, -1):
        ans *= 10
        if not n:
            continue
        for j in range(b-1, 0, -1):
            if n >= j*(b**i):
                ans += j
                n -= j*(b**i)
                break
    return ans


n = int(input("Number : "))
b = int(input("Base   : "))
print("{}-ary  : {}".format(b, n_ary(n, b)))
