class Solution:
    def uniqueOccurrences(self, array):
        map = {}
        for i in range(0, len(array)):
            num = array[i]
            if (num in map.keys()):
                map[num] += 1
            else:
                map[num] = 1

        memo = {}
        for k in map.keys():
            count_num_occurances = map[k]
            if (count_num_occurances in memo.keys()):
                return False

            memo[count_num_occurances] = True

        return True