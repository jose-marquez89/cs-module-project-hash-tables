"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = range(50)
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


cache = {}


def sum_diff(nums, func_cache, skip_duplicates=True):
    # create number combination system
    combo = [0, 0]
    complete = []

    # build cache for additions, cache duplicates
    while combo[0] < len(nums):
        add_combo = (nums[combo[0]], nums[combo[1]])

        # skip duplicates
        if (add_combo[1], add_combo[0]) in complete and skip_duplicates:
            if combo[1] == (len(nums) - 1):
                combo[1] = 0
                combo[0] += 1
            else:
                combo[1] += 1
            continue
        else:
            a = f(add_combo[0])
            b = f(add_combo[1])
            value = a + b

            if value in func_cache:
                func_cache[value]["pos_nums"].append((add_combo[0],
                                                      add_combo[1]))
                func_cache[value]["pos_vals"].append((a, b))
            else:
                func_cache[value] = {"pos_nums": [(add_combo[0],
                                                   add_combo[1])],
                                     "pos_vals": [(a, b)],
                                     "neg_nums": None,
                                     "neg_vals": None}
            if combo[1] == (len(nums) - 1):
                combo[1] = 0
                combo[0] += 1
            else:
                combo[1] += 1

            complete.append(add_combo)

    combo = [0, 0]

    # add subractions to cache if the result exists
    while combo[0] < len(nums):
        sub_combo = (nums[combo[0]], nums[combo[1]])
        c = f(sub_combo[0])
        d = f(sub_combo[1])
        value = c - d
        if value in func_cache:
            if func_cache[value]["neg_nums"] is not None:
                func_cache[value]["neg_nums"].append((sub_combo[0],
                                                      sub_combo[1]))
                func_cache[value]["neg_vals"].append((c, d))
            else:
                func_cache[value]["neg_nums"] = [(sub_combo[0], sub_combo[1])]
                func_cache[value]["neg_vals"] = [(c, d)]
        if combo[1] == (len(nums) - 1):
            combo[1] = 0
            combo[0] += 1
        else:
            combo[1] += 1

    # for total in cache
    for value in func_cache:
        if func_cache[value]["neg_nums"]:
            for x in range(len(func_cache[value]["pos_nums"])):
                for y in range(len(func_cache[value]["neg_nums"])):
                    a = func_cache[value]["pos_nums"][x][0]
                    b = func_cache[value]["pos_nums"][x][1]
                    c = func_cache[value]["neg_nums"][y][0]
                    d = func_cache[value]["neg_nums"][y][1]
                    va = func_cache[value]["pos_vals"][x][0]
                    vb = func_cache[value]["pos_vals"][x][1]
                    vc = func_cache[value]["neg_vals"][y][0]
                    vd = func_cache[value]["neg_vals"][y][1]

                    print(f"f({a}) + f({b}) = f({c}) - f({d})  "
                          f"{va} + {vb} = {vc} - {vd}")


if __name__ == '__main__':
    sum_diff(q, cache, skip_duplicates=False)
