# Circular primes
def is_prime(number):  # function that checks if numbers is prime
    if number == 1:
        return False
    for y in range(2, round(number ** 0.5) + 1):
        if number % y == 0:
            return False
    return True


def is_circular_prime(number):  # function that checks if number is circular prime
    number = list(str(number))
    for x in number:
        number.insert(0, number[-1])
        number.pop(-1)
        if not is_prime(int("".join(number))):
            return False
    return True


nums = list()  # list with circular prime numbers
for i in range(1, 1_000_000):  # looping numbers
    if is_circular_prime(i):
        nums.append(i)
print(len(nums))  # Output: 55
 