def wordBreakUtil(line, dictionary, matrixT):
    szlen = len(line)
    if szlen == 0:
        return 1
    if line in dictionary:
        matrixT[line] = 1
        return matrixT[line]
    if line in matrixT.keys():
        return matrixT[line]
    for i in range(1, szlen):
        flag = 0
        tempstr = line[0:i]
        if tempstr in dictionary:
            flag = 1

        if flag and wordBreakUtil(line[i:], dictionary, matrixT):
            matrixT[line] = 1
            return matrixT[line]
    matrixT[line] = 0
    return matrixT[line]
matrixT = {}
dictionary = ["ab", "bcd", "b", "a"]
line = "abcd"
print(wordBreakUtil( line, dictionary, matrixT))