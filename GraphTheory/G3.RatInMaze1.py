def findPathUtil(i, j, m, n, s, vis, ans):
    if i < 0 or j < 0 or i >= n or j >= n:
        return
    if vis[i][j] == 1 or m[i][j] == 0:
        return
    if i == n - 1 and j == n - 1:
        ans.append(s)

    vis[i][j] = 1

    findPathUtil(i - 1, j, m, n, s + 'U', vis, ans)
    findPathUtil(i, j + 1, m, n, s + 'R', vis, ans)
    findPathUtil(i + 1, j, m, n, s + 'D', vis, ans)
    findPathUtil(i, j - 1, m, n, s + 'L', vis, ans)
    vis[i][j] = 0

def findPath(m, n):
    # code here
    vis = [[0 for j in range(n)] for i in range(n)]
    ans = list()
    s = ""
    findPathUtil(0, 0, m, n, s, vis, ans)
    return sorted(ans)
m = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
n = 4
print(findPath(m, n))