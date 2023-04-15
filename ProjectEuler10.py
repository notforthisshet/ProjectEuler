# Summation of primes
def is_prime(number):  # creating a function that checks if number is prime or not
    if number == 1:
        return False  # 1 isn't a prime number
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False  # returning False if number has divisor
    return True  # returning True if number doesn't have any divisors


summ = 0  # sum of prime numbers
for x in range(1, 2_000_000):  # looping numbers
    if is_prime(x):
        summ += x  # updating sum of prime numbers
print(summ)  # printing sum of prime numbers
# Output: 142913828922
