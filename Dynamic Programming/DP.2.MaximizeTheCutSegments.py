def isSubsetSum(N, arr, sum):
    matrixT = [[0 for i in range(sum+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                matrixT[i][j] = max(arr[i-1] + matrixT[i][j-arr[i-1]], matrixT[i-1][j])
            else:
                matrixT[i][j] = matrixT[i-1][j]

    return matrixT

arr = [int(item) for item in input("Enter no of ways a ROD can be cut :").split()]
sum = int(input("enter lenth of ORD :"))

print(isSubsetSum(len(arr), arr, sum))
