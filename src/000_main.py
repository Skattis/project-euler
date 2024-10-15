from src.utils.primes import sieve

if __name__ == "__main__":
    n = int(input("Primes up to the following number:\n"))
    print(sieve(n))