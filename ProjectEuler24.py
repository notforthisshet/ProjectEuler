# Lexicographic permutations
from itertools import permutations
alph = "0123456789"  # alph for permutations
numbers = sorted(list(map(int, list(map("".join, list(permutations(alph)))))))  # lmao
print(numbers[999999])  # Output: 2783915460
