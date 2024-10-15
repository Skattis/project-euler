def pal(word: str):
    lenN = len(word)
    middle = lenN // 2
    if lenN % 2 == 0:
        return word[:middle] == word[middle:][::-1]
    mPOne = middle + 1
    return word[:middle] == word[mPOne:][::-1]


def largest_pal_prod():
    a = 1000
    lst = []
    while a > 1:
        a -= 1
        b = 1000
        while b > 1:
            b -= 1
            if pal(str(a * b)):
                lst.append(a * b)
    return max(lst)

# alternativ
def palind_three_digit_m():
    max = 0
    for z1 in range(100, 1000):
        for z2 in range(100, 1000):
            z = str(z1 * z2)
            laenge_z = len(z)
            if laenge_z == 5:
                if z[0] == z[4] and z[1] == z[3]:  # if true -> palindromic number
                    if max < int(z):
                        max = int(z)

            if laenge_z == 6:  # if true, palindromic number
                if z[0] == z[5] and z[1] == z[4] and z[2] == z[3]:
                    if max < int(z):
                        max = int(z)

    return max

if __name__ == "__main__":
    print(largest_pal_prod())
