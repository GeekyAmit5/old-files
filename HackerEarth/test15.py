a = [1, 2, 3, 4]


def subsets(s):
    global ans
    if s not in ans:
        ans.append(s)
    for i in range(len(s)):
        subsets(s[:i]+s[i+1:])


ans = []
subsets(a)
print(ans)
