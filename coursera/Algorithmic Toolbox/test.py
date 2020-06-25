import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def max(l):
    m = l[0]
    for i in l:
        if m < i:
            m = i
    return m


def max_product(l):
    m = max(l)
    l.remove(m)
    k = m*max(l)
    l.append(m)
    return k


while True:
    l = [random.randint(1, 100) for x in range(random.randint(2, 10))]
    if max_product(l) != max_pairwise_product(l):
        print(max_product(l), max_pairwise_product(l))
        break
    print(max_product(l))
