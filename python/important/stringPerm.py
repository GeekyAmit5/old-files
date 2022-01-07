import sys

# sys.setrecursionlimit(100000)


# occurence of letter x in text
def occurences(text, x):
    c = 0
    for i in text:
        if i == x:
            c += 1
    return c


def perm():
    global text, ans
    if len(ans) == len(text):
        print("".join(ans))
    else:
        for i in text:
            if occurences(text, i) > occurences(ans, i):
                ans.append(i)
                perm()
                ans.pop()


text = input('Enter the string: ')
ans = []
perm()
