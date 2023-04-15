# 10001st prime
def is_prime(number):  # creating a function that checks if number is prime or not
    if number == 1:
        return False  # 1 isn't prime number
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False  # returning False if number has divisor
    return True  # returning True if number doesn't have any divisors


count = 0  # counter of prime numbers
num = 1
while True:  # looping numbers
    if is_prime(num):
        count += 1
    if count == 10001:
        break  # breaking on 10001st prime number
    num += 1
print(num)  # printing 10001st prime number
# Output: 104743
