# import myfunctions as mf
import math


def isPrime(x):
    if x == 1 or (x > 2 and x % 2 == 0):
        return False
    elif x == 2:
        return True
    else:
        for i in range(3, math.floor(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
    return True

# def multiplicity(x, y):
#     m = 0
#     while not x % y:
#         x = x // y
#         m += 1
#     return m


def multiplicity(x, y):
    if x % y:
        return 0
    return 1+multiplicity(x/y, y)


def primeFactorisation(x):
    print(x, "=", end="")
    p, j = 1, 2
    while True:
        if not x % j and isPrime(j):
            print(" {}^{}".format(j, multiplicity(x, j)), end=" ")
            p *= j ** multiplicity(x, j)
            if p == x:
                break
            else:
                print(" x ", end="")
        j += 1


n = int(input("Enter a number : "))
primeFactorisation(n)
print("\nDone!")
