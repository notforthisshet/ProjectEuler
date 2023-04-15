# Sum square difference
numbers1 = sum([x ** 2 for x in range(1, 101)])  # finding sum of squares
numbers2 = sum([y for y in range(1, 101)]) ** 2  # finding square of sum
print(numbers2 - numbers1)  # printing the difference
# Output: 25164150
