arr1 = [str(item) for item in input("Enter arr1:").split()]
arr2 = [str(item) for item in input("Enter arr2:").split()]

def EditDistance(A, B):
    n = len(A)
    m = len(B)

    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        matrixT[i][0] = i
    for j in range(m+1):
        matrixT[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                matrixT[i][j] = matrixT[i-1][j-1]
            else:
                matrixT[i][j] = min(matrixT[i-1][j], matrixT[i][j-1], matrixT[i-1][j-1]) + 1
    return matrixT[n][m]

print(EditDistance(arr1, arr2))
