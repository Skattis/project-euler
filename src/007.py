from src.utils.primes import prime


def n_thPrime(n):
    if n == 1:
        return 2
    counter = 1
    x = 3
    while True:
        if prime(x):
            counter += 1
            if counter == n:
                return x
        x += 2

if __name__ == "__main__":
    print(n_thPrime(10_001))
