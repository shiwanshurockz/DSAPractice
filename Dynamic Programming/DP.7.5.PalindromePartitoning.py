import sys
import time
arr = str(input("Enter string: "))
matrixT = [[-1 for i in range(501)] for j in range(501)]
palindromeT = [[-1 for i in range(501)] for j in range(501)]

def isPalinfrome(str, i, j):
    if (i >= j):
        return True
    while(i < j):
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True

def palindromePartioning(arr, i, j):
    if i >= j:
        return 0
    mn = sys.maxsize
    if matrixT[i][j] != -1:
        return matrixT[i][j]

    if palindromeT[i][j] == -1:
        if isPalinfrome(arr, i, j) is True:
            palindromeT[i][j] = True
            return 0
        else:
            palindromeT[i][j] = False
    else:
        if palindromeT[i][j] is True:
            return 0

    for k in range(i, j):
        if matrixT[i][k] != -1:
            left = matrixT[i][k]
        else:
            if palindromeT[i][k] == -1:
                if isPalinfrome(arr, i, k) is True:
                    left = 0
                    matrixT[i][k] = left
                    palindromeT[i][k] = True
                else:
                    left = palindromePartioning(arr, i, k)
                    matrixT[i][k] = left
                    palindromeT[i][k] = False

        if matrixT[k+1][j] != -1:
            right = matrixT[k + 1][j]
        else:
            if palindromeT[k+1][j] == -1:
                if isPalinfrome(arr, k+1, j) is True:
                    right = 0
                    matrixT[k + 1][j] = right
                    palindromeT[i][k] = True
                else:
                    right = palindromePartioning(arr, k + 1, j)
                    matrixT[k + 1][j] = right
                    palindromeT[i][k] = False

        tempans = 1 + left + right
        if mn > tempans:
            mn = tempans
    matrixT[i][j] = mn
    return mn

# store starting time
begin = time.time()
print(palindromePartioning(arr, 0, len(arr) -1))
# store end time
end = time.time()
# total time taken
print(f"Total runtime of the program is {end - begin}")