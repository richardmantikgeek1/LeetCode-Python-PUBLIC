class Solution:
    def largestAltitude(self, gain):
        prefix_sum = 0
        left_sum = []
        for i in range(0, len(gain)):
            num = gain[i]

            left_sum.append(prefix_sum)
            prefix_sum += num
        left_sum.append(prefix_sum)

        return max(left_sum)