t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    se = (n(n+1)/2) % (10**9 + 7)
    m = m//2
    so = (m(m+1)/2) % (10**9 + 7)
    ans = se + so + ((se*so) % (10**9 + 7))
    print(ans % (10**9+7))
