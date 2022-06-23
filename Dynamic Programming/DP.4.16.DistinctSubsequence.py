arr1 = [str(item) for item in input("Enter arr1:").split()]
arr2 = [str(item) for item in input("Enter arr2:").split()]

def DistinctSubsequence(S, T):
    n = len(S)
    m = len(T)
    if n == 0 and m == 0:
        return 1
    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        matrixT[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if S[i-1] == T[j-1]:
                matrixT[i][j] = matrixT[i-1][j-1] + matrixT[i-1][j]
            else:
                matrixT[i][j] = matrixT[i-1][j]
    return matrixT[n][m]

print(DistinctSubsequence(arr1, arr2))
