import myfunctions as mf
import random as rd

def polynomial(l):  #prints a polynomial
    if len(l)>0:
        print(l[0], end="")
    if len(l) > 1:
        for i in range(1, len(l)):
            print(" + {}x^{}".format(l[i], i), end="")
        print(" = 0")

def derivative(l):  # differentiate a polynomial
    d = []
    for i in range(1,len(l)):
        d.append(l[i]*i)
    return d

def enter():  # takes a polynomial from user
    l = []
    n=int(input("Enter Degree : "))
    print("Enter Coefficients : ")
    for i in range(n+1):
        l[i].append(int(input()))
    return l

def zero(l):  # returns list of rational zeros
    z, k,n = [], 0,1
    while not l[k]:
        z.append(0)
        k += 1
    while not l[-n]:
        n+=1
    for i in mf.divList(l[k]):
        for j in mf.divList(l[-n]):
            if i / j not in z:
                if rootCheck(l, i / j):
                    z.append(i / j)
                if rootCheck(l, -(i / j)):
                    z.append(-(i / j))
    return z

def rootCheck(l, x):  # checks if number is root of that polynomial
    s = 0
    for i in range(len(l)):
        s += l[i] * pow(x,i)
    return s == 0

def add(p,q):
    z=[]
    for i in range (min(len(p),len(q))):
        z.append(p[i]+q[i])
    for i in range (min(len(p),len(q)),max(len(p),len(q))):
        if len(p)<=len(q):
            z.append(q[i])
        else:
            z.append(p[i])
    return z