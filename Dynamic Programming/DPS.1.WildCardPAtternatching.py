def wildCardUtil(pattern, string, matrixT, i, j):
    if i == -1 and j == -1:
        return 1
    if i == -1:
        for k in range(j):
            if pattern[k] != "*":
                return 0
        return 1
    if j == -1:
        return 0

    if matrixT[i][j] != -1:
        return matrixT[i][j]

    if pattern[j] == string[i] or pattern[j] == "?":
        matrixT[i][j] = wildCardUtil(pattern, string, matrixT, i - 1, j - 1)
        return matrixT[i][j]
    elif pattern[j] == "*":
        a = wildCardUtil(pattern, string, matrixT, i - 1, j)
        b = wildCardUtil(pattern, string, matrixT, i, j - 1)
        matrixT[i][j] = a or b
        return matrixT[i][j]
    else:
        matrixT[i][j] = 0
        return matrixT[i][j]

def wildCard(pattern, string):
    # Code here
    n = len(string)
    m = len(pattern)
    matrixT = [[-1 for j in range(m)] for i in range(n)]
    return wildCardUtil(pattern, string, matrixT, n - 1, m - 1)
pattern = "ba*a?"
string = "baaabab"
print(wildCard(pattern, string))