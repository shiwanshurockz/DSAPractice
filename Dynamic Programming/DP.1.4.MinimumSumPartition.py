arr = [int(item) for item in input("Enter Array :").split()]

def isSubsetSum(n, arr, sum):
    matrixT = [[False for i in range(sum+1)] for j in range(n+1)]

    for i in range(n+1):
        matrixT[i][0] = True
    for j in range(1, sum+1):
        matrixT[0][j] = False

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if (arr[i-1] <= j):
                matrixT[i][j] = matrixT[i-1][j-arr[i-1]] or matrixT[i-1][j]
            else:
                matrixT[i][j] = matrixT[i-1][j]
    return matrixT


sumarr = sum(arr)
length = len(arr)
solMat = isSubsetSum(len(arr), arr, sumarr)
min_val = sumarr
vector = []
for i in range(1, sumarr+1):
    if solMat[length][i]:
        vector.append(i)
for i in range(len(vector)//2):
    min_val = min(min_val, (sumarr - (2 * vector[i])))
print(min_val)

