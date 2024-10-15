# from time import perf_counter as pfc


# def solve(n):
#     isEven = lambda x: x % 2 == 0
#     even = lambda x: x // 2
#     odd = lambda x: 3 * x + 1
#     start_n = n
#     count = 1

#     while n != 1:
#         n = even(n) if isEven(n) else odd(n)
#         count += 1

#     return start_n, count


# def solve_for_z_n(z):
#     number, max_chain = None, 0
#     for i in range(1, z):
#         s = solve(i)
#         if max_chain < s[1]:
#             number, max_chain = s[0], s[1]
#     return number, max_chain


# start = pfc()
# print(solve_for_z_n(1_000_000))
# print(pfc() - start)