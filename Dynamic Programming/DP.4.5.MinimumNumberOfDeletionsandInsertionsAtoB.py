s1 = input("Enter A:")
s2 = input("Enter B:")

def transformAtoB(s1, s2):
    n = len(s1)
    m = len(s2)

    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                matrixT[i][j] = 1+matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])
    return (n - matrixT[n][m])+(m-matrixT[n][m])

print(transformAtoB(s1, s2))