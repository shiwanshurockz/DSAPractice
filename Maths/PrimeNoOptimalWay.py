A = [int(item) for item in input("Enter Array :").strip().split()]
print(A)
#sieve of eratosthenes
def returnPrimeList( A):
    primeno = []
    prime = [True for i in range(A+1)]
    p = 2
    while  p*p <= A :
        if prime[p] is True:
            for i in range(p**2, A+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for i in range(A+1):
        if prime[i] is True:
            primeno.append(i)
    return primeno





print(returnPrimeList(A))
