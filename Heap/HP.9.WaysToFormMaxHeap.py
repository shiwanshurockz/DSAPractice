import math
M = 1000000007
A= 5
ncrmap = dict()
Adp = [-1 for i in range(A+1)]
def nCr(n, r):
    if r > n:
        return 0
    if n <= 1:
        return 1
    if r == 0:
        return  1
    if r == 1:
        return n
    if (n,r) in ncrmap.keys():
        return ncrmap[(n, r)]
    val = nCr(n-1, r-1) + nCr(n-1, r)
    ncrmap[(n, r)] = val
    return val

def getLeft(n):
    if n == 1:
        return 0
    h = int(math.log2(n))
    numh = (1 << (h-1))
    lastElements = n - ((1 << h)-1)
    return  (numh-1) + min(numh, lastElements)

def NoOfWays(A):
    if A <= 1:
        return 1
    if Adp[A] != -1:
        return Adp[A]

    L = getLeft(A)
    R = A - 1 - L
    ncr = nCr(A-1,L) % M
    ans = (ncr * (NoOfWays(L)%M) * (NoOfWays(R)%M))%M
    Adp[A] = ans
    return ans

print(NoOfWays(A))