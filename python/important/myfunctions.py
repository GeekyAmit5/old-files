# all functions are here
# gcd ,lcm ,rev num ,prime, sum of div, fibo ,fact , popping and det and trace, divList , redump , print a polynomial,

import time
import math
import cmath as cm
import datetime as dt
import random as rd
from functools import lru_cache


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


def sumOfProperDivisors(x):
    sum = 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            sum += i
    return sum


@lru_cache()
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def gcd(x, y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


def multiplicity(x, y):  # by recursion
    if x % y:
        return 0
    return 1+multiplicity(x/y, y)


def gcd(x, y):  # by recursion
    r = x % y
    if not r:
        return y
    return gcd(y, r)


def lcm(x, y):
    return x * y // gcd(x, y)


def revNum(x):
    s = 0
    while x > 0:
        r = x % 10
        s = s * 10 + r
        x = x // 10
    return s


def threesquares(m):
    if m <= 0:
        return False
    a = 0
    while m >= 4**a * 7:
        b = 0
        while m >= 4**a * (8*b + 7):
            if m == 4**a * (8*b + 7):
                return False
            b += 1
        a += 1
    return True


def repfree(s):
    return len(s) == len(set(s))


def hillvalley(l):
    c = 0
    increament = True
    decreament = True
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            if increament:
                c += 1
            decreament = True
            increament = False
        else:
            if decreament:
                c += 1
            decreament = False
            increament = True
    return c == 2


def popping(l, n):
    p = []
    for i in range(1, len(l)):
        p.append([])
        for j in range(len(l)):
            if j == n:
                continue
            p[i - 1].append(l[i][j])
    return p


def det(l):
    if len(l) == 1:
        return l[0][0]
    else:
        s = 0
        for i in range(len(l)):
            s += pow(-1, i) * l[0][i] * det(popping(l, i))
        return s


def transpose(m):
    l = [[0 for x in range(len(m))]for y in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[i])):
            l[j][i] = m[i][j]
    return l


def trace(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i][i]
    return sum


def trace1(l):  # by recursion
    if len(l):
        return l[0][0] + trace(popping(l, 0))
    return 0


def divList(x):
    l = [1]
    if abs(x) == 1:
        return l
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            l.append(i)
    l.append(abs(x))
    return l


def remdup(l):  # takes a list and remove all duplicate entries
    j = 0
    for i in l:
        if i in l[:j]:
            l.pop(j)
            remdup(l)
        j += 1
    return l


def polynomial(l):  # prints a polynomial
    print(l[0], end="")
    if len(l) > 1:
        for i in range(1, len(l)):
            print("+{}x^{}".format(l[i], i), end="")
    print(" = 0")
