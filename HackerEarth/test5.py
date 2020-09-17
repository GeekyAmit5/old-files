from functools import lru_cache


@lru_cache
def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)


n = 0
while True:
    if not fact(n) % 1000:
        print(n)
        break
    n += 1
