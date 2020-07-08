def no_dups(s):
    if s == "":
        return s
    cache = {}

    s = s.split()
    order_count = 0
    for word in s:
        if word in cache:
            continue
        cache[word] = order_count
        order_count += 1

    sorted_words = list(cache.items())
    sorted_words.sort(key=lambda x: x[1])

    words, counts = zip(*sorted_words)

    return ' '.join(words)




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
