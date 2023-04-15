# Smallest multiple
from math import gcd  # importing the greatest common divisor
divisor = 1  # setting the first divisor
for i in range(1, 21):
    divisor *= i // gcd(divisor, i)
print(divisor)  # printing divisor
# Output: 232792560
