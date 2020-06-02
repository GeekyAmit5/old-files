import time


def derangement():
    global ans, total, depth
    if depth == n:
        print(ans)
        total += 1
    else:
        for i in list:
            if i not in ans and i != depth + 1:
                ans.append(i)
                depth += 1
                derangement()
                ans.pop()
                depth -= 1


n = int(input("Enter the value of n : "))
list = [x+1 for x in range(n)]
ans = []
total, depth = 0, 0
t0 = time.time()
derangement()
t1 = time.time()
print("Total :", total)
print("Time :", t1-t0)
