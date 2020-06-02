# Decimal into binary


import math


def binary(n):
    if not n:
        return n
    ans = 0
    for i in range(round(math.log(n, 2)), -1, -1):
        ans *= 10
        if n >= 2**i:
            ans += 1
            n -= 2**i
    return ans


print("Binary :", binary(int(input("Number : "))))
