# Longest Collatz sequence
def collatz(number):  # a function that counts the length of collatz sequence
    sequence = [number]  # collatz sequence
    while True:  # looping numbers
        if number % 2 == 0:
            number /= 2
            sequence.append(int(number))
        else:
            number = 3 * number + 1
            sequence.append(int(number))
        if number == 1:
            break
    return len(sequence)  # returning length of sequence


collatz_sequences = dict()  # dictionary with lengths of sequences and their start numbers
for i in range(1, 1_000_000):  # looping numbers
    collatz_sequences[collatz(i)] = i
print(collatz_sequences[max(collatz_sequences.keys())])  # Output: 837799
