S = input("Enter String :")

def minimumNumberOfDeletions(S):
    s1 = S
    s2 = S[::-1]
    n = len(S)
    m = len(S)
    matrixT = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                matrixT[i][j] = 1+ matrixT[i-1][j-1]
            else:
                matrixT[i][j] = max(matrixT[i-1][j], matrixT[i][j-1])

    lps = matrixT[n][m]
    return len(S)-lps

print(minimumNumberOfDeletions(S))