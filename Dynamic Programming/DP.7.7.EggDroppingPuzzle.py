import sys
matrixT = [[-1 for i in range(201)] for j in range(201)]
e, f = map(int, input().strip().split())

def Solve(e, f):

    if f == 0 or f ==1:
        return f
    if e == 1:
        return f

    if matrixT[e][f] != -1:
        return matrixT[e][f]

    mn = sys.maxsize
    for k in range(1, f+1):

        if matrixT[e-1][k-1] != -1:
            low = matrixT[e-1][k-1]
        else:
            low = Solve(e-1, k-1)
            matrixT[e-1][k-1] = low

        if matrixT[e][f-k] != -1:
            high = matrixT[e][f-k]
        else:
            high = Solve(e, f-k)
            matrixT[e][f-k] = high
        temp = 1+max(low, high)
        mn = min(mn, temp)

    matrixT[e][f] = mn
    return mn

print(Solve(e, f))