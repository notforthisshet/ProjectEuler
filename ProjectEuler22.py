# Names scores
f = open("p022_names.txt")  # Opening file
for i in f:
    names = sorted(i.replace('"', '').split(","))  # creating a sorted list of names
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # alph for counting name points
points = 0  # total points

for word in names:  # looping words
    name_points = 0
    for letter in word:  # looping letter in word
        name_points += alph.index(letter) + 1
    points += name_points * (names.index(word) + 1)

print(points)  # Output: 871198282
