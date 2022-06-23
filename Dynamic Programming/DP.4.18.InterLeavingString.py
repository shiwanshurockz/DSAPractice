s1 = input("EnterS1:")
s2 = input("EnterS2:")
s3 = input("EnterS3:")
cache = {}
def check(s1, s2, s3, l1, l2, l3, p1, p2, p3):
    if p3 == l3:
        return 1 if p1 == l1 and p2 == l2 else 0
    if (p1, p2, p3) in cache:
        return cache[(p1, p2, p3)]
    if p1 == l1:
        cache[(p1, p2, p3)] = 0 if s2[p2] != s3[p3] else check(s1, s2, s3, l1, l2, l3, p1, p2+1, p3+1)
        return cache[(p1, p2, p3)]
    if p2 == l2:
        cache[(p1, p2, p3)] = 0 if s1[p1] != s3[p3] else check(s1, s2, s3, l1, l2, l3, p1+1, p2, p3+1)
        return cache[(p1, p2, p3)]
    one = 0
    two = 0
    if s1[p1] == s3[p3]:
        one = check(s1, s2, s3, l1, l2, l3, p1+1, p2, p3+1)
    if s2[p2] == s3[p3]:
        two = check(s1, s2, s3, l1, l2, l3, p1, p2+1, p3+1)

    cache[(p1, p2, p3)] = one or two
    return cache[(p1, p2, p3)]

def IsInterleavingstring(s1, s2, s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    if l3 != l1+l2:
        return 0
    else:
        return check(s1, s2, s3, l1, l2, l3, 0, 0, 0)

print(IsInterleavingstring(s1, s2, s3))