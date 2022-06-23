str1 = input("Enter S1")
str2 = input("Enter S2")
map = {}

def Scramble(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) == 0 and len(str2) == 0:
        return True

    if str1 == str2:
        return True
    if len(str1) <= 1:
        return False

    tempStr = ""
    tempStr += str(str1)
    tempStr += " "
    tempStr += str(str2)

    if tempStr in map.keys():
        return map[tempStr]

    flag = False
    n = len(str1)

    for k in range(1, n):
        if (Scramble(str1[-k:], str2[:k]) and Scramble(str1[:-k], str2[k:])) or \
                (Scramble(str1[:k], str2[:k]) and Scramble(str1[k:], str2[k:])):
            flag = True
            break
    map[tempStr] = flag
    return flag


print(Scramble(str1, str2))