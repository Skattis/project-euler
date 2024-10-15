from src.utils.primes import sieve

if __name__ == "__main__":
    n = 2_000_000
    print(sum(sieve(n)))
