arr = input("Enter string :")
map = {}

def EvaluateExpression(arr, i, j, isTrue):
    if i > j:
        return False
    if i == j:
        if isTrue is True:
            return arr[i] == 'T'
        else:
            return arr[i] == 'F'

    tempStr = ""
    tempStr += str(i)
    tempStr += " "
    tempStr += str(j)
    tempStr += " "
    tempStr += str(isTrue)

    if tempStr in map.keys():
        return map[tempStr]

    ans = 0
    for k in range(i+1, j, 2):
        lT = EvaluateExpression(arr, i, k-1, True)
        lF = EvaluateExpression(arr, i, k-1, False)
        rT = EvaluateExpression(arr, k+1, j, True)
        rF = EvaluateExpression(arr, k+1, j, False)

        if arr[k] == '&':
            if isTrue is True:
                ans = ans + lT*rT
            else:
                ans = ans + (lT*rF) + (lF*rT) + (lF*rF)
        elif arr[k] == '|':
            if isTrue is True:
                ans = ans + (lT*rT) + (lT*rF) + (lF*rT)
            else:
                ans = ans + lF*rF
        elif arr[k] == '^':
            if isTrue is True:
                ans = ans + (lT*rF) + (lF*rT)
            else:
                ans = ans + (lT*rT) + (lF*rF)

    map[tempStr] = ans
    return map[tempStr]

def cnttrue(A):
    elem = [A[i] for i in range(0, len(A), 2)]
    oper = [A[i] for i in range(1, len(A), 2)]
    n = len(elem)

    dp = [[[0, 0] for p in range(n)] for p in range(n)]
    for i in range(n):
        tmp = elem[i] == 'T'
        dp[i][i][0], dp[i][i][1] = int(tmp), int(not tmp)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            for k in range(i, j):
                op = oper[k]
                pre, suf = sum(dp[i][k]), sum(dp[k + 1][j])
                if op == '&':
                    dp[i][j][0] += dp[i][k][0] * dp[k + 1][j][0]
                    dp[i][j][1] += pre * suf - dp[i][k][0] * dp[k + 1][j][0]
                elif op == '|':
                    dp[i][j][0] += pre * suf - dp[i][k][1] * dp[k + 1][j][1]
                    dp[i][j][1] += dp[i][k][1] * dp[k + 1][j][1]
                else:
                    dp[i][j][0] += dp[i][k][0] * dp[k + 1][j][1] + dp[i][k][1] * dp[k + 1][j][0]
                    dp[i][j][1] += dp[i][k][0] * dp[k + 1][j][0] + dp[i][k][1] * dp[k + 1][j][1]
    return dp[0][-1][0]

print(EvaluateExpression(arr, 0, len(arr)-1, True)% 1003)
print(cnttrue(arr))

