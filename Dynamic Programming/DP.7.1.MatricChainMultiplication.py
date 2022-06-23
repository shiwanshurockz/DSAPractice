import sys
arr = [int(item) for item in input("Enter array elements :").split()]
matrixT = [[-1 for i in range(501)] for j in range(501)]

def matrixChainMultiplication(arr, i, j):
    if i >= j:
        return 0
    if matrixT[i][j] != -1:
        return matrixT[i][j]

    mn = sys.maxsize
    for k in range(i, j):
        temAns = matrixChainMultiplication(arr, i, k) + matrixChainMultiplication(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
        if mn > temAns:
            mn = temAns
    matrixT[i][j] = mn
    return mn

print(matrixChainMultiplication(arr, 1, len(arr)-1))
