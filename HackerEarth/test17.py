def sticks(n):
    if n//10 == 0:
        if n == 0 or n == 9 or n == 6:
            return 6
        elif n == 1:
            return 2
        elif n == 2 or n == 3 or n == 5:
            return 5
        elif n == 4:
            return 4
        elif n == 7:
            return 3
        elif n == 8:
            return 7
    else:
        return sticks(n % 10) + sticks(n//10)


def solve():
    global m, ans, s
    m = max(m, ans)
    for i in range(10):
        # temp = sticks(i)
        if sticks(i) <= s:
            ans = ans*10 + i
            s -= sticks(i)
            solve()
            s += sticks(i)
            ans = (ans-i)//10


t = int(input())
for i in range(t):
    n = int(input())
    s = sticks(n)
    m = n
    ans = 0
    solve()
    print(m)
