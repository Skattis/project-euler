# from time import perf_counter as pfc


# def create_grid(r, c):
#     return [[1 for col in range(c + 1)] for row in range(r + 1)]


# def solve(grid):

#     for r, row in enumerate(grid):
#         for c, _ in enumerate(row):
#             if r == 0 or c == 0:
#                 continue
#             grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

#     return grid[-1][-1]


# grid = create_grid(20, 20)
# start = pfc()
# print(solve(grid))
# print(pfc() - start)