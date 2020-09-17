def check(s):
    val = len(s)
    change = 0
    for i in range(val-1):
        if s[i] != s[i+1]:
            change += 1
            if change > 2:
                return False
    return True
q = ['abaababbbaaaabaaab']
while q:
    val = len(q[0])
    if val < 4:
        print(val)
        break
    elif check(q[0]):
        print(val)
        break
    else:
        for i in range(val):
            s = q[0][:i]+q[0][i+1:]
            if s not in q:
                q.append(s)
        q.pop(0)
