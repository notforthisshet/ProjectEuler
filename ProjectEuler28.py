# Number spiral diagonals
spiral_size = 1001  # the size of spiral
print(sum(4 * i * i - 6 * (i - 1) for i in range(3, spiral_size + 1, 2)) + 1)  # mixing formulas. Output: 669171001
