n = 2
a = [1, 2]
max = -1


def solve(l1, r1, l2, r2):
    if 0 <= l1 <= r1 < l2 <= r2 <= n-1:
        pass
    else:
        return
    global max
    ans = sum(a[l1:r1+1]) ^ sum(a[l2:r2+1])
    if max < ans:
        max = ans
    if r2 < n-1:
        solve(l1, r1, l2, r2+1)
    elif l2 < r2:
        solve(l1, r1, l2+1, l2+1)
    elif r1 < l2-1:
        solve(l1, r1+1, r1+2, r1+2)
    else:
        solve(l1+1, l1+1, l1+2, l1+2)
solve(0, 0, 1, 1)
print(max)
