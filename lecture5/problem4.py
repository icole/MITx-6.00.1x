def gcdIter(a, b):
    gcd = 1
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

print str(gcdIter(6, 12))
