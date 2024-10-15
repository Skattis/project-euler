import os

fname = os.path.join("EulersA", "008.txt")
with open(fname, mode="r", encoding="UTF-8") as f:
    number_string = "".join(f.read().split("\n"))


def valid(i, length):
    return i + 12 < length


def product(n_string):
    res = 1
    for n in n_string:
        res *= int(n)
    return res


products = []

for i in range(len(number_string)):
    if valid(i, len(number_string)):
        prod = product(number_string[i : i + 13])
        products.append(prod)

result = max(products)

print(result)
