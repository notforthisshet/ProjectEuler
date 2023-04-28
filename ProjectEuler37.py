# Truncatable primes
def is_prime(number):  # function that checks if number is prime
    if number == 1:
        return False
    for d in range(2, round(number ** 0.5) + 1):
        if number % d == 0:
            return False
    return True


def is_truncatable_prime(number):  # function that checks if prime number is truncatable
    if len(str(number)) == 1:
        return False
    if not is_prime(number):
        return False
    num1 = list(str(number))
    num2 = list(str(number))
    for x in range(len(num1) - 1):
        num1.pop(0)
        num2.pop(-1)
        if not is_prime(int("".join(num1))) or not is_prime(int("".join(num2))):
            return False
    return True


nums = list()  # list with truncatable prime numbers
for i in range(1, 1_000_000):  # looping numbers
    if is_truncatable_prime(i):
        nums.append(i)
print(sum(nums))  # Output: 748317
