# Even Fibonacci numbers
fib_nums = [1, 2]  # creating a list with fibonacci numbers
while fib_nums[-1] < 4_000_000:  # looping while the last number is below 4 millions
    fib_nums.append(fib_nums[-1] + fib_nums[-2])  # filling the list
print(sum([x for x in fib_nums if x % 2 == 0]))  # printing the sum of all even numbers in list
# Output: 4613732
