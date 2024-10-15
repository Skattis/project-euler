def pythagoreanTriplet(a, b, c):
    return a * a + b * b == c * c


def special_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if pythagoreanTriplet(a, b, c):
                    if a + b + c == 1000:
                        return a * b * c


prod = special_triplet()
print(prod)
