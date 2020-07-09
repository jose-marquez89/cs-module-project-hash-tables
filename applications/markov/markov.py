import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

sequence_cache = {}
words = words.split()

# build cache
for w in range(len(words)-1):
    if words[w] in sequence_cache:
        sequence_cache[words[w]].append(words[w+1])
    else:
        sequence_cache[words[w]] = [words[w+1]]

# group stop and start words
consolidated_groups = sequence_cache.keys()
start = []
for w in consolidated_groups:
    if w.istitle():
        start.append(w)


def print_nonsense(start_list, word_cache):
    stop_punc = ('.', '?', '!', '"')
    word = random.choice(start_list)
    all_words = list(word_cache.keys())
    stop = False
    print(word, end=' ')
    word = random.choice(all_words)
    while not stop:
        if word in start_list:
            word = random.choice(all_words)
            continue
        elif word[-1] in stop_punc:
            stop = True
            print(word)
        else:
            print(word, end=' ')
            word = random.choice(all_words)


if __name__ == "__main__":
    for i in range(5):
        print_nonsense(start, sequence_cache)
