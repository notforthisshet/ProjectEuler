# 1000-digit Fibonacci number
a = 0  # previous fib number
b = 1  # current fib number
count = 0  # fib numbers counter
while True:  # looping numbers
    count += 1
    a, b = b, a + b
    if len(str(a)) == 1000:
        print(count)  # Output: 4782
        break
