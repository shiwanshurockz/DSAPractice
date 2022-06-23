def hammingDistance(n1, n2):
    x = n1 ^ n2
    setBits = 0

    while (x > 0):
        setBits += x & 1
        x >>= 1

    return setBits

def hammingPairwiseDistance( A):
    if len(A) == 1 or len(A) == 0:
        return 0
    count = 0
    map = {}
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                hamcount = hammingDistance(A[i], A[j])
                tempKey = str(i)+" "+str(j)
                if tempKey not in map.keys():
                    map[tempKey] = hamcount
    count = sum(map.values())
    return count

def sumBitDifference(A):
    n = len(A)
    ans = 0
    for i in range(0, 32):
        count = 0
        for j in range(n):
            if A[j] & 1<<i:
                count += 1
        ans += (count * (n-count) * 2)
    return ans