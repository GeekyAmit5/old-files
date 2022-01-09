import random
import time


def sod1(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans


def sod2(x):
    if x//10:
        return x % 10+sod2(x//10)
    return x


for i in range(10):
    n = random.randint(1, 10000000)
    print('\n', n, sep='')
    print(sod1(n))
    print(sod2(n))
    time.sleep(0.5)
