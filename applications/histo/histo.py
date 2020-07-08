from word_counter import word_count

cache = {}

with open("robin.txt", "r") as robin:
    for line in robin:
        word_count(line, cache)

# sort cache
sorted_cache = list(cache.items())
sorted_cache.sort(key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    for word, count in sorted_cache:
        print(f"{word.ljust(20)}{'#'*count}")
