def one(s):
    if not s:
        return '0'
    elif s[0] == '1':
        return s
    else:
        return one(s[1:])
def solve(i, j):
    if i >= n-2 or j >= n-1:
        return -1
    x = one(a[:i])
    y = one(a[i:j])
    z = one(a[j:])
    if y == z:
        if x == y:
            return int(x, 2)
        else:
            return solve(i+1, j)
    else:
        return solve(i, j+1)
t = int(input())
for i in range(t):
    n = int(input())
    a = input().replace(' ', '')
    print(a)
    print(solve(1, 2))
