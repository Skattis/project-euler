def fib(n):  # Recursion Error
    def go(n, a, b):
        if n == 1:
            return a
        return go(n - 1, a + b, a)

    return go(n, 1, 1)


def evenFibN(n):
    a, b = 1, 1
    result = 0
    while True:
        a, b = a + b, a
        if a > n:
            break
        if a % 2 == 0:
            result += a
    return result


if __name__ == "__main__":
    print(evenFibN(4_000_000))
