def maxCities(grid, n, m):
    # code here
    # returned value will be printed
    max = 0
    mat = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= i+a < n and 0 <= j+b < m and grid[i+a][j+b] != '*':
                            mat[i+a][j+b] = 1
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                l = 0
                q = [(i, j)]
                while q:
                    for a in range(-1, 2):
                        for b in range(-1, 2):
                            if 0 <= q[0][0] + a < n and 0 <= q[0][1] + b < m:
                                q.append((q[0][0] + a, q[0][1] + b))
                    l += 1
                    q.pop(0)
                if l > max:
                    max = l
    return max


'''
Input:
2
5 5
....*
.....
..*..
.....
.....
1 2
**

Output:
10
0
'''
