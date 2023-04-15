# Special Pythagorean triplet
p = 1000  # setting perimeter


def triplet(p):  # creating a function that returns a * b * c
    for a in range(1, p + 1):  # looping a
        for b in range(1, p + 1):  # looping b
            c = p - a - b  # looping c
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c  # returns a * b * c if a, b and c are Pythagorean triplet


print(triplet(p))  # printing the function product
# Output: 31875000
