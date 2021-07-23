# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import random

from package.module import naive_sum, std_sum, numpy_sum


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.summands = list(range(10000))

    def time_naive(self):
        result = naive_sum(self.summands)

    def time_std(self):
        result = std_sum(self.summands)

    def time_numpy(self):
        result = numpy_sum(self.summands)


class ComparisonSuite:
    """
    An example comparing the timings of different functions with the same inputs.
    """
    params = ([naive_sum, std_sum, numpy_sum])
    param_names = ("method")

    def setup(self, method):
        self.summands = [random.random() for i in range(1000000)]

    def time_sums(self, method):
        result = method(self.summands)


class MemSuite:
    def mem_list(self):
        return [0] * 256
