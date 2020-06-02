import time


def isJumping(n):
    if n < 10:
        return True
    else:
        return (abs((n % 10) - ((n//10) % 10)) == 1) and isJumping(n//10)


total = 0
n = int(input("n = "))
t0 = time.time()
print("Jumping numbers upto {} are :".format(n))
for i in range(n+1):
    if isJumping(i):
        print(i)
        total += 1
print('Total :', total)
t1 = time.time()
print("Time  :", t1-t0)
