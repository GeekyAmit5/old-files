def sub():
    global total
    if len(B) == length:
        print(set(B))
        total += 1
    else:
        for i in A:
            if not len(B) or i > B[-1]:
                B.append(i)
                sub()
                B.pop()


A = {x for x in range(int(input("No. of Elements? ")))}
# A = {'a', 'b', 'c', 'd'}
print("Set".ljust(10), ":", A)
print("Subsets".ljust(10), ":")
B = []
length = 0
total = 0
for i in range(len(A)+1):
    length = i
    sub()
print("Total :", total)
