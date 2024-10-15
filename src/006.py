def gauss_sum(n):
    return n * (n + 1) // 2


def sumSquareDiff(n):
    x = sum(i**2 for i in range(1, n + 1))
    y = gauss_sum(n) ** 2
    return abs(x - y)


print(sumSquareDiff(100))
