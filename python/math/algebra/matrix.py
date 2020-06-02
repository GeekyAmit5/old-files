
import cmath
import myfunctions as mf

n = int(input("Enter the Order of the Square Matrix: "))
a = [[0 for x in range (n)] for y in range(n)]
print("Enter the elements Row-wise : ")
for i in range (n):
    for j in range(n):
        a[i][j]=int(input())


def EVCheck(a,x):
    for i in range (n):
        a[i][i]-=x
    c=mf.det(a)
    for i in range(n):
        a[i][i] += x
    if c:
        return False
    return True

print("The Eigen Values are : ")
if n==2:
    print((mf.trace(a)+ cmath.sqrt((mf.trace(a))**2 - 4 * mf.det(a))) /2)
    print((mf.trace(a) - cmath.sqrt((mf.trace(a))**2 - 4 * mf.det(a)))/2)
else :
    n1 = 10000
    i = -n1
    while i <= n1:
        if (EVCheck(a, i)):
            print(i)
        i += 0.25
