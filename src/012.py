# from time import perf_counter as pfc


# def num_divisors(n):
#     divisors = 0
#     for i in range(1, int(n**0.5 + 1)):
#         if n % i == 0:
#             divisors += 2
#     return divisors


# tri = 0
# lst = []
# zahl = 500

# start = pfc()
# for i in range(1, 40000):
#     tri = tri + i
#     divisors = num_divisors(tri)
#     if divisors > zahl:
#         print(tri)
#         break
# print(pfc() - start)