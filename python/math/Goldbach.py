# every even number can be written as sum of two primes
# this is a conjecture


import math
import time


def isPrime(x):
    if x == 1 or (x > 2 and x % 2 == 0):
        return False
    elif x == 2:
        return True
    else:
        for i in range(3, round(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
    return True


n = int(input("Enter the value of n : "))
t0 = time.time()
for i in range(6, n+1, 2):
    for j in range(3, i // 2+1, 2):
        if isPrime(j) and isPrime(i-j):
            print("{} = {} + {}".format(i, j, i - j))
            break
    else:
        print(i)
        break
t1 = time.time()
print("Time :", t1-t0)
