# Pandigital products
pans = set()  # set with pandigital numbers
for x in range(10000):  # looping numbers
    for i in range(1, round(x ** 0.5) + 1):
        if x % i == 0:
            if "".join(sorted(str(x) + str(i) + str(x // i))) == "123456789":  # checking if number is pandigital
                pans.add(x)
print(sum(pans))  # Output: 45228
