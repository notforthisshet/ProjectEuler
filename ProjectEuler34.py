# Digit factorials
from math import factorial
summ = 0  # sum of numbers
for i in range(3, 100_001):  # looping numbers
    if sum([factorial(int(x)) for x in list(str(i))]) == i:
        summ += i
print(summ)  # Output: 40730
