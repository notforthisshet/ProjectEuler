# Amicable numbers
def div_sum(number):  # a function that calculates the sum of divisors of number
    divisors = {1}
    for x in range(2, round(number ** 0.5) + 1):
        if number % x == 0:
            divisors.add(x)
            divisors.add(number // x)
    return sum(divisors)


fr_numbers = set()  # creating a set with amicable numbers
for i in range(1, 10000):  # looping numbers
    if i == div_sum(div_sum(i)) and i != div_sum(i):
        fr_numbers.add(i)
        fr_numbers.add(div_sum(i))

print(sorted(fr_numbers))  # printing the list with amicable numbers
print(sum(fr_numbers))  # Output: 31626
