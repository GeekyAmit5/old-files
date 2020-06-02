# jumping numbers
import time


def jumping(n):
    global total
    q = [x for x in range(0, 11) if x <= n]
    # q = [x for x in range(0,min(11,n+1))] #alternate way
    while q:
        if 0 < q[0] % 10 < 9:
            l = q[0]*10 + q[0] % 10 - 1
            r = q[0]*10 + q[0] % 10 + 1
            if r <= n:
                if l not in q:
                    q.append(l)
                if r not in q:
                    q.append(r)
            elif l <= n and l not in q:
                q.append(l)
        elif not q[0] % 10:
            l = q[0]*10 + 1
            if l <= n and l not in q:
                q.append(l)
        else:
            l = q[0]*10 + 8
            if l <= n and l not in q:
                q.append(l)
        print(q[0])
        total += 1
        q.pop(0)


total = 0
n = int(input("Enter the value of n : "))
t0 = time.time()
print("Jumping numbers upto {} are :".format(n))
jumping(n)
print("Total :", total)
t1 = time.time()
print("Time  :", t1-t0)
