def list(n): return [n-x for x in range(n)]


def partition(x):
    global total
    if sum(parts) == n:
        print(parts)
        total += 1
    else:
        for i in list(x):
            if sum(parts)+i <= n:
                parts.append(i)
                partition(i)
                parts.pop()


n = int(input("Enter a Number : "))
parts = []
total = 0
partition(n)
print('Total =', total)
