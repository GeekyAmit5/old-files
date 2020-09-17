def f(a, b, c):
    return 6050408 + a*10**5 + b*10**3 + c*10


max = -1
for i in range(10):
    for j in range(6):
        for k in range(6-j):
            if (i+j+k)**2 > max and not f(j, k, i) % 72:
                max = (i+j+k)**2
print(max)
