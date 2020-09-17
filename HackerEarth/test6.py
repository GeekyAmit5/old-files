# code
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    while a:
        m = max(a)
        sum += m
        a.remove(m)
        try:
            a.remove(m-1)
        except:
            pass
    print(sum)

    Correct Answer.Correct Answer
Execution Time: 0.02

# code
t = int(input())
for i in range(t):
    s = input()
    ans = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'gfg':
            ans += 1
    if ans:
        print(ans)
    else:
        print(-1)

Correct Answer.Correct Answer
Execution Time: 0.03

# code
t = int(input())
for i in range(t):
    l1, l2 = map(int, input().split())
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    if sum(c1) >= sum(c2):
        print("C1")
    else:
        print("C2")

Correct Answer.Correct Answer
Execution Time: 0.02


def gcd(x, y):
    if not x % y:
        return y
    else:
        return gcd(y, x % y)


def isCoprime(x, l):
    for i in l:
        if gcd(x, i) != 1:
            return False
    return True


def solve(n):
    global ans, done
    if done:
        return
    elif len(ans) == n:
        done = True
    else:
        for i in a:
            if isCoprime(i, ans):
                ans.append(i)
                solve(n)
                ans.pop()


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n, 0, -1):
        done = False
        ans = []
        solve(i)
        if done:
            print(i)
            break
