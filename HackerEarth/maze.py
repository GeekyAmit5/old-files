
l, k = map(int, input().split())
b = int(input())
c = list(map(int, input().split()))

ans = 0


def solve(b, d):
    global ans
    if d == k+1:
        ans += 1
    else:
        if 0 <= b+c[d-1] < l:
            solve(b+c[d-1], d+1)
        if 0 <= b-c[d-1] < l:
            solve(b-c[d-1], d+1)


solve(b, 1)
print(ans)
