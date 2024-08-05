from heapq import _heapify_max, _heappop_max, _siftdown_max

class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        digits_array = [int(d) for d in num_str]
        even_nums_heap = [d for d in digits_array if d % 2 == 0]
        _heapify_max(even_nums_heap)
        odd_nums_heap = [d for d in digits_array if d % 2 == 1]
        _heapify_max(odd_nums_heap)
        for i in range(0, len(digits_array)):
            num = digits_array[i]
            if (num % 2 == 0):
                digits_array[i] = _heappop_max(even_nums_heap)
            else:
                digits_array[i] = _heappop_max(odd_nums_heap)
        return int(''.join([str(d) for d in digits_array]))