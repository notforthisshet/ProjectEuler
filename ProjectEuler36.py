# Double-base palindromes
count = 0  # sum of all double-base palindromes
for number in range(1, 1_000_000):  # looping numbers
    if str(number) == str(number)[::-1] and bin(number)[2:] == bin(number)[2:][::-1] and bin(number)[2:][0] != "0":
        count += number
print(count)  # Output: 872187
