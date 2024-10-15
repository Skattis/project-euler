from math import sqrt


def prime(n):
    if n < 4:
        return True
    elif n == 5 or n == 7:
        return True
    elif n < 11:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(5, int(sqrt(n)) + 2, 2):
        if n % x == 0:
            return False
    return True

def sieve_inefficient(n: int):
    numbers = [i for i in range(2,n+1)]
    primes = []
    while numbers:
        p = numbers.pop(0)
        numbers = list(filter(lambda x: x % p != 0, numbers))
        primes.append(p)
    return primes

def sieve(n: int):
    """
    Once you reach a prime, all smaller multiples of a prime (2p, 3p) 
    have already been marked as non_prim by smaller prime factors

    When your looking for for primes:
    if a number is not a prime it can be factored as n = a*b
    at least one factor must be smaller than sqrt(n)

    All multiples of primes have already been marked as False once you reach sqrt(n)
    """
    is_prime = [True] * (n+1)
    p = 2

    while p * p <= n:
        if is_prime[p]:
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n+1) if is_prime[p]]

    return primes