c = {}


def expensive_seq(x, y, z, cache):
    trio = (x, y, z)
    if trio in cache:
        return cache[trio]
    if x <= 0:
        cache[trio] = y + z
        return cache[trio]
    else:
        cache[trio] = (expensive_seq(x-1, y+1, z, cache) +
                       expensive_seq(x-2, y+2, z*2, cache) +
                       expensive_seq(x-3, y+3, z*3, cache))

        return cache[trio]


if __name__ == "__main__":
    for i in range(10):
        a = expensive_seq(i*2, i*3, i*4, c)
        print(f"{i*2} {i*3} {i*4} = {a}")

    print(expensive_seq(150, 400, 800, c))
