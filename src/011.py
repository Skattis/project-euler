import os

fname = os.path.join("src","011.txt")

def prods(row, col):
    pass

with open(fname, mode="r", encoding="UTF-8") as f:
    lines = f.read().split("\n")
    for line in lines:
        numbers = line.split(" ")
        numbers = list(map(int, numbers))

    products = []
    for row, line in enumerate(numbers):
        for col, n in enumerate(line):
            prods(row, col)
            products.extend()


# very bad solution, refactor
# from math import prod

# fname = "Problem011.txt"
# with open(fname, "r") as f:
#     grid = [list(map(int, line.rstrip().split())) for line in f.readlines()]

# lst = []

# for row_i, row in enumerate(grid):
#     bot_too_close = row_i > len(grid) - 4
#     for colm_i, number in enumerate(row):
#         edge_too_close = colm_i > len(grid[colm_i]) - 4
#         left_to_close = colm_i < 3
#         if not edge_too_close and not bot_too_close:
#             b = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i + 1][colm_i],
#                     grid[row_i + 2][colm_i],
#                     grid[row_i + 3][colm_i],
#                 ]
#             )
#             e = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i][colm_i + 1],
#                     grid[row_i][colm_i + 2],
#                     grid[row_i][colm_i + 3],
#                 ]
#             )
#             a = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i + 1][colm_i + 1],
#                     grid[row_i + 2][colm_i + 2],
#                     grid[row_i + 3][colm_i + 3],
#                 ]
#             )

#             lst.append(b)
#             lst.append(e)
#             lst.append(a)

#         elif not bot_too_close:
#             b = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i + 1][colm_i],
#                     grid[row_i + 2][colm_i],
#                     grid[row_i + 3][colm_i],
#                 ]
#             )
#             lst.append(b)
#         elif not edge_too_close:
#             e = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i][colm_i + 1],
#                     grid[row_i][colm_i + 2],
#                     grid[row_i][colm_i + 3],
#                 ]
#             )
#             lst.append(e)
#         if not left_to_close and not bot_too_close:
#             l = prod(
#                 [
#                     grid[row_i][colm_i],
#                     grid[row_i + 1][colm_i - 1],
#                     grid[row_i + 2][colm_i - 2],
#                     grid[row_i + 3][colm_i - 3],
#                 ]
#             )
#             lst.append(l)


# print(max(lst))
