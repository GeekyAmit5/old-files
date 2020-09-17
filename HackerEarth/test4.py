t = 50
b = 62
r = 0
max = -1


def solve():
    global t, b, r, max
    if max < r:
        max = r
    if b >= 5 and t >= 2:
        r += 1
        t -= 2
        b -= 5
        solve()
        t += 2
        b += 5
        r -= 1
    if b >= 3 and t >= 3:
        r += 1
        t -= 3
        b -= 3
        solve()
        t += 3
        b += 3
        r -= 1


solve()
print(max)
