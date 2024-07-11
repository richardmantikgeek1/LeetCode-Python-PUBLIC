class Solution:
    def pivotIndex(self, array):
        left_sum    = deque()
        right_sum   = deque()
        prefix_sum  = 0

        for i in range(0, len(array)):
            num = array[i]

            left_sum.append(prefix_sum)
            prefix_sum += num

        prefix_sum = 0
        for i in range(len(array) - 1, -1, -1):
            num = array[i]

            right_sum.appendleft(prefix_sum)
            prefix_sum += num

        for i in range(0, len(left_sum)):
            if (left_sum[i] == right_sum[i]):
                return i
        
        return -1