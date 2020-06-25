def max_product(l):
    m = max(l)
    l.remove(m)
    return m*max(l)


n = int(input())
l = [int(x) for x in input().split()]
print(max_product(l))
