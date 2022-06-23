arr = [int(item) for item in input("Enter arr elements :").split()]

def isSubsetSum(N, arr, sum):
    matrixT = [[False for i in range(sum+1)]
               for j in range(N+1)]
    for i in range(N+1):
        matrixT[i][0] = True
    for j in range(1, sum+1):
        matrixT[0][j] = False

    for i in range(1, N+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                matrixT[i][j] = matrixT[i-1][j-arr[i-1]] or matrixT[i-1][j]
            else:
                matrixT[i][j] = matrixT[i-1][j]
    if matrixT[N][sum]:
        return "YES"
    else:
        return "NO"

def isEqualSumPartition(N, arr):
    sum = 0
    for i in range(N):
        sum += arr[i]
    if sum % 2 == 0:
        return isSubsetSum(N, arr, sum//2)
    else:
        return "NO"

print(isEqualSumPartition(len(arr), arr))