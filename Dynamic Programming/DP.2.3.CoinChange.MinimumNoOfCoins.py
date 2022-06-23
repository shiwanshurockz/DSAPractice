import sys



def minNoOFCoins(N, arr, sum):
    matrixT = [[0 for j in range(sum+1)] for i in range(N+1)]

    for j in range(sum+1):
        matrixT[0][j] = sys.maxsize-1

    for i in range(1, N+1):
        matrixT[i][0] = 0

    for j in range(1, sum+1):
        if j % arr[0] == 0:
            matrixT[1][j] = j//arr[0]
        else:
            matrixT[1][j] = sys.maxsize-1

    for i in range(2, N+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                matrixT[i][j] = min(matrixT[i][j-arr[i-1]] + 1, matrixT[i-1][j])
            else:
                matrixT[i][j] = matrixT[i-1][j]
    return matrixT[N][sum]

def maximizeTheCuts():
    # code here
    arr = [2,1,1]
    sum = 4
    N = 3
    matrixT = [[0 for j in range(sum + 1)] for i in range(N + 1)]

    for j in range(sum + 1):
        matrixT[0][j] = -1

    for i in range(1, N + 1):
        matrixT[i][0] = 0

    for j in range(1, sum + 1):
        if j % arr[0] == 0:
            matrixT[1][j] = j // arr[0]
        else:
            matrixT[1][j] = -1

    for i in range(2, N + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                matrixT[i][j] = max(matrixT[i][j - arr[i - 1]] + 1, matrixT[i - 1][j])
            else:
                matrixT[i][j] = matrixT[i - 1][j]
    return matrixT

print(maximizeTheCuts())

