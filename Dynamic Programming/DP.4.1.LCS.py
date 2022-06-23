arrA = [str(item) for item in input("Enter array 1 :").split()]
arrB = [str(item) for item in input("Enter array 2 :").split()]

def LCSRecursive(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    else:
        if(x[n-1] == y[m-1]):
            return 1 + LCSRecursive(x, y, n-1, m-1)
        else:
            return max(LCSRecursive(x, y, n-1, m), LCSRecursive(x, y, n, m-1))

def LCSTopDown(x, y, n, m):
    matrixT = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1] and i!=j:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])
    return matrixT[n][m]

def LongestCommonSubstringTopDown(x, y, n, m):
    max = 0
    matrixT = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
                if matrixT[i][j] > max:
                    max = matrixT[i][j]
            else:
                matrixT[i][j] = 0
    return max

print(LCSTopDown(arrA, arrB, len(arrA), len(arrB)))



