def countPsUtil(i, j, string, matrixT):
    if i > j:
        return 0
    if i == j:
        return 1
    if matrixT[i][j] != -1:
        return matrixT[i][j]
    if string[i] == string[j]:
        matrixT[i][j] = 1 + countPsUtil(i+1, j, string, matrixT) + countPsUtil(i, j-1, string, matrixT)
        return matrixT[i][j]
    else:
        matrixT[i][j] = countPsUtil(i+1, j, string, matrixT) + countPsUtil(i, j-1, string, matrixT) - countPsUtil(i+1, j-1, string, matrixT)
        return matrixT[i][j]


def countPs(string):
    # Code here
    n = len(string)
    matrixT = [[-1 for j in range(n)] for i in range(n)]
    return countPsUtil(0, n-1, string, matrixT) % 1000000007
