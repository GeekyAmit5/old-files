def gcd(x, y):
    r = x % y
    if not r:
        return y
    return gcd(y, r)


x, y = map(int, input().split())
print(x*y//gcd(x, y))
