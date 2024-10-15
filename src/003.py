from src.utils.primes import prime
from colorama import Fore, init

init()



def prime_factors(n):
    prime_factors = []
    prm = 2
    while n != 1:
        if n % prm == 0:
            prime_factors.append(prm)
            n = n // prm
        else:
            for i in range(prm + 3, n + 1):
                if prime(i):
                    prm = i
                    break
    print(Fore.CYAN + f"{prime_factors}")
    return prime_factors


# number = int(input(Fore.CYAN + "Please input an Integer:\n" + Fore.GREEN))
# p = prime(number)
# a = Fore.GREEN if p else Fore.RED
# print(Fore.CYAN + f"Is {number} a prime" + a + f" {p}")

if __name__ == "__main__":
    c = 600851475143
    print(prime_factors(c)[-1])
