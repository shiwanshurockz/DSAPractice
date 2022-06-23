arr1 = [str(item) for item in input("Enter arr1:").split()]
arr2 = [str(item) for item in input("Enter arr2:").split()]

def RegexMatch(S, P):
    n = len(S)
    m = len(P)
    cache = {}
    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i >= n and j >= m:
            return 1
        if j >= m:
            return 0
        match = i < n and (S[i] == P[j] or P[j] == ".")
        if j+1 < m and P[j+1] == "*":
            cache[(i, j)] = (match and dfs(i+1, j)) or dfs(i, j+2)
            return cache[(i, j)]
        if match:
            cache[(i, j)] = dfs(i+1, j+1)
            return cache[(i, j)]
        if P[j] == "*":
            cache[(i, j)] = 1
        else:
            cache[(i, j)] = 0
        return cache[(i, j)]
    return dfs(0, 0)


def RegexMatchBottomUp(P, S):
    n = len(S)
    m = len(P)

    matrixT = [[False for j in range(m+1)] for i in range(n+1)]
    matrixT[0][0] = True
    for j in range(1, m+1):
        if P[j-1] == "*":
            matrixT[0][j] = matrixT[0][j-2]
        else:
            matrixT[0][j] = False

    for i in range(1, n+1):
        for j in range(1, m+1):
            if S[i-1] == P[j-1] or P[j-1] == ".":
                matrixT[i][j] = matrixT[i-1][j-1]
            elif P[j-1] == "*":
                if matrixT[i][j-2]:
                    matrixT[i][j] = True
                elif S[i-1] == P[j-2] or P[j-2] == ".":
                    matrixT[i][j] = matrixT[i-1][j]
                else:
                    matrixT[i][j] = False
            else:
                matrixT[i][j] = False
    return matrixT[i][j]

print(RegexMatchBottomUp(arr1, arr2))