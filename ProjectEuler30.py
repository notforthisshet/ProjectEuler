# Digit fifth powers
summ = 0  # the sum of numbers
for i in range(2, 1_000_000):  # looping numbers
    if sum([int(x) ** 5 for x in list(str(i))]) == i:
        summ += i
print(summ)  # Output: 443839
