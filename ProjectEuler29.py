# Distinct powers
numbers = set()  # set with numbers to count the amount
for a in range(2, 101):  # looping a
    for b in range(2, 101):  # looping b
        numbers.add(a ** b)
print(len(numbers))  # Output: 9183
