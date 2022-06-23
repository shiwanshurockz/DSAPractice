s1 = input("enter 1")
s2 = input("enter 2")

def LCSMatrixPrint(s1, s2):
    n = len(s1)
    m = len(s2)

    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1] and i != j:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])
    lcsString = ""

    i = n
    j = m
    while i > 0 and j > 0:
        if matrixT[i][j] == matrixT[i-1][j-1]+1:
            lcsString = lcsString + s1[j-1]
            i = i-1
            j = j-1
        else:
            if matrixT[i-1][j] > matrixT[i][j-1]:
                i = i-1
            else:
                j = j-1

    return lcsString[::-1]

print(LCSMatrixPrint(s1, s2))