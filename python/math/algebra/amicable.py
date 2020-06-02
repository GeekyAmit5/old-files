# to find amicable numbers in a given range
import time
import python.important.myfunctions as mf

l = []
c = 0
m = int(input("Enter Lower Bound : "))
n = int(input("Enter Upper Bound : "))
print('The amicable numbers from {} to {} are : '.format(m, n))
t0 = time.time()
for i in range(m, n+1):
    if not i in l and i != mf.sumOfProperDivisors(i) and i == mf.sumOfProperDivisors(mf.sumOfProperDivisors(i)):
        l.append(mf.sumOfProperDivisors(i))
        print(i, "\t", mf.sumOfProperDivisors(i))
        c += 1

if not c:
    print('No such numbers are found in the given range')
else:
    print("Total :", c)
t1 = time.time()
print("Time :", t1-t0)
