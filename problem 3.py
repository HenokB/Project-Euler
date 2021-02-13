def problem_3(x):
    factors = []
    for i in range (2,int(sqrt(x))):
        if x % i == 0:
            factors.append(i)
            factors.append(int(x/i))
    factors.sort()
    prime_factors = factors
    remove = []

    for i in range (len(factors)-1,0,-1):
        a = i-1
        for j in range (a,-1,-1):
            if prime_factors[i] % prime_factors[j] == 0:
                remove.append(prime_factors[i])
            a = a - 1

    prime_factors = list(set(set(prime_factors) - set(remove)))

    return prime_factors


prime_factors = problem_3(600851475143)
prime_factors.sort()
print (max(prime_factors))