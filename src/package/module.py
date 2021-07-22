#  import numpy as np


def naive_sum(summands):
    sum = 0
    for summand in summands:
        sum += summand
    return sum


def std_sum(summands):
    return sum(summands)


def numpy_sum(summands):
    #  return np.sum(summands)
    return "skipped to not require numpy"
