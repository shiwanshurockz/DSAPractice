def isSubsetSum(N, arr, sum):
    N = N+1
    M = sum+1
    matrixT = ([[False for i in range(M)]
               for i in range(N)])
    for i in range(N):
        matrixT[i][0] = True

    for i in range(1, sum):
        matrixT[0][i] = False

    for i in range(1, N):
        for j in range(1, M):
            if arr[i-1] <= j:
                matrixT[i][j] = matrixT[i - 1][j - arr[i-1]] or matrixT[i - 1][j]
            else:
                matrixT[i][j] = matrixT[i-1][j]
    if matrixT[N-1][M-1]:
        return 1
    else:
        return 0



arr = [int(item) for item in input("Enter arr :").split()]
sum = int(input("Enter Sum :"))

print(isSubsetSum(len(arr), arr, sum))

