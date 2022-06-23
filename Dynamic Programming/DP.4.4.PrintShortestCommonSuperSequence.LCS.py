s1 = input("enter 1")
s2 = input("enter 2")

def LCSMatrixPrint(s1, s2):
    n = len(s1)
    m = len(s2)

    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])
    lcsString = ""

    i = n
    j = m
    while i > 0 or j > 0:
        if s1[i-1] == s2[j-1]:
            lcsString = lcsString + s1[i-1]
            i = i-1
            j = j-1
        else:
            if matrixT[i-1][j] > matrixT[i][j-1]:
                i = i-1
            else:
                if matrixT[i][j-1] > matrixT[i-1][j]:
                    j = j-1

    return lcsString[::-1]

def SCSMatrixPrint(s1, s2):
    n = len(s1)
    m = len(s2)

    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])
    lcsString = ""

    i = n
    j = m
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcsString = lcsString + s1[i-1]
            i = i-1
            j = j-1
        else:
            if matrixT[i-1][j] > matrixT[i][j-1]:
                lcsString = lcsString + s1[i-1]
                i = i-1
            else:
                lcsString = lcsString + s2[j - 1]
                j = j - 1
    while(i > 0):
        lcsString = lcsString+s1[i-1]
        i = i-1
    while (j > 0):
        lcsString = lcsString + s2[j-1]
        j = j - 1

    return lcsString[::-1]


print(LCSMatrixPrint(s1, s2))
