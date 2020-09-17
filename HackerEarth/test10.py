
def maxCities(grid, n, m):
    a = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] == '.':
                            a.add((i+x, j+y))

    mat = [[0 for i in range(m)] for j in range(n)]

    def dfs(i, j):
        mat[i][j] = 1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (i+x, j+y) in a and not mat[i+x][j+y]:
                    b.add((i+x, j+y))
                    dfs(i+x, j+y)

    ans = 0
    for i, j in a:
        if not mat[i][j]:
            b = set()
            b.add((i, j))
            dfs(i, j)
            ans = max(ans, len(b))
    return ans


grid = ['....*', '.....', '..*..', '.....', '.....']

print(maxCities(grid, 5, 5))
