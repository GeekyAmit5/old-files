def sub():
    global B, total
    if len(B) == length:
        C = B[:]
        C.sort()
        if C not in subsets:
            subsets.append(C)
            print(set(C))
            total += 1
    else:
        for i in A:
            if i not in B:
                B.append(i)
                sub()
                B.pop()


n = int(input('Enter the number of elements: '))
A = [x for x in range(n)]
# n = 4
# A = {'a', 'b', 'c', 'd'}
print("Set :", set(A))
print("Subsets :")
B = []
subsets = []
length = 0
total = 0
for i in range(n+1):
    length = i
    sub()
print("Total :", total)
