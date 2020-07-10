"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

func_cache = {}

def sum_diff(nums):
    # build cache

    slots = [0, 0, 0, 0]
    prev = 3
    next = 1
    position = 3
    limit = 0

    while slots[0] < len(nums):
        combo = (nums[slots[0]], nums[slots[1]],
                 nums[slots[2]], nums[slots[3]])
        left = f(combo[0]) + f(combo[1])
        right = f(combo[2]) + f(combo[3])
        if left == right:
            func_cache[combo] = (left, right)

        if position == limit:
            slots[position] = next
            position = 3
            limit += 1
        else:
            slots[position] = next
            position -= 1
            slots[prev] = next - 1
            prev -= 1

        if limit == len(slots):
            next += 1
            limit = 0

        print(slots)

if __name__ == '__main__':
    sum_diff(q)
