# Large sum
# The list of numbers is large, so I'd recommend using file instead of 100 lines of code
with open("numbers.txt") as f:  # opening file
    numbers = list(map(int, f.readlines()))  # converting to list
print(str(sum(numbers))[0:10])  # Output: 5537376230
