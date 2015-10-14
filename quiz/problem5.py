def primesList(N):
    primes = []
    num = 2
    while num <= N:
        prime = True
        i = num - 1
        while i > 1:
            if num % i == 0:
                prime = False
                break
            i -= 1
        if prime:
            primes.append(num)
        num += 1
    return primes

print primesList(20)
