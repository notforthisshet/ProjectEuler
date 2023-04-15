# Largest prime factor
def is_prime(number):  # creating a function that checks if number is prime or not
    if number == 1:
        return False  # 1 isn't a prime number
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False  # returning False if number has any divisor
    return True  # returning True if number doesn't have any divisors


divisors = set()  # creating a set with divisors of number
for x in range(1, round(600851475143 ** 0.5) + 1):  # filling the set with divisors of number
    if 600851475143 % x == 0:
        divisors.add(x)
        divisors.add(600851475143 // x)
print(max([div for div in divisors if is_prime(div)]))  # finding the max divisor in prime divisors of number
# Output: 6857
