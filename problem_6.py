import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 1:
        return (ints[0], ints[0])

    t_min = ints[0]
    t_max = ints[0]
    for i in ints:
        if t_min > i:
            t_min = i
        if t_max < i:
            t_max = i
    return (t_min, t_max)


# Example Test Case of Ten Integers
l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 99) == get_min_max(l)) else "Fail")
