def divisible(x, n):
    if x % 2 != 0:
        return False
    for i in range(3, n):
        if x % i != 0:
            return False
    return True


def smallestMultiple(n):
    x = 20
    while True:
        x += 2
        if divisible(x, n):
            return x


result = smallestMultiple(20)
print(result)
