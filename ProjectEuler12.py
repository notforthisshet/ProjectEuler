# Highly divisible triangular number
def divisors_count(number):  # function that counts the amount of number divisors
    divisors = {number}  # set with divisors
    for d in range(1, round(number ** 0.5) + 1):  # looping numbers
        if number % d == 0:
            divisors.add(d)
            divisors.add(number // d)
    return len(divisors)  # returning amount of divisors


num = 0  # triangular number
for i in range(1, 1_000_000):  # looping triangular numbers
    num += i
    if divisors_count(num) > 500:
        print(num)  # Output: 76576500 (576 divisors)
        break
