coin = [int(item) for item in input("Enter the Denominations available :").split()]
N = int(input("Entet the amount required :"))

def isSubsetSumUnbounded(N, arr, sum):
    matrixT = [[0 for j in range(sum+1)] for i in range(N+1)]

    for k in range(1, N+1):
        matrixT[k][0] = 1

    for i in range(1, N+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                matrixT[i][j] = matrixT[i][j-arr[i-1]] + matrixT[i-1][j]
            else:
                matrixT[i][j] = matrixT[i-1][j]

    return  matrixT[N][sum]

print(isSubsetSumUnbounded(len(coin), coin, N))