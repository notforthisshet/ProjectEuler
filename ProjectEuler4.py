# Largest palindrome product
palindromes = set()  # creating a set with palindromes
for x in range(100, 1000):  # looping 3 digits numbers
    for y in range(100, 1000):
        if str(x * y) == str(x * y)[::-1]:
            palindromes.add(x * y)  # adding the number in set if number is palindrome
print(max(palindromes))  # printing the max palindrome number
# Output: 906609
