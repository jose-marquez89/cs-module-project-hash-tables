# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt", "r") as ctext:
    words = ctext.read()

char_counts = {}
most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# count words
for char in words:
    if char.isalpha():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

# get frequencies
frequencies = {}
char_len = len(char_counts)
for char in char_counts.keys():
    frequencies[char] = char_counts[char] / char_len

# sort characters by frequency
freq_sorted = list(frequencies.items())
freq_sorted.sort(key=lambda x: x[1], reverse=True)

# create key
key = {freq_sorted[c][0]: most_frequent[c]
       for c in range(len(freq_sorted))}


def decode(text, decode_key):
    for c in text:
        if c in decode_key:
            print(decode_key[c], end='')
        else:
            print(c, end='')


if __name__ == "__main__":
    decode(words, key)
