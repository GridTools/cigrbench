# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

from package.module import naive_sum, std_sum, numpy_sum


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.summands = list(range(10000))

    def time_naive(self):
        sum = naive_sum(self.summands)

    def time_std(self):
        sum = std_sum(self.summands)

    def time_numpy(self):
        sum = numpy_sum(self.summands)


class MemSuite:
    def mem_list(self):
        return [0] * 256
