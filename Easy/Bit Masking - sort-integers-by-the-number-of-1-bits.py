class Solution:
    def sortByBits(self, array):
        num_to_count_1s_map = {}
        # num_to_count_1s_map[0] = 0
        # num_to_count_1s_map[1] = 1
        # num_to_count_1s_map[2] = 1
        # num_to_count_1s_map[3] = 2
        # num_to_count_1s_map[4] = 1
        # num_to_count_1s_map[5] = 2
        # num_to_count_1s_map[6] = 2
        # num_to_count_1s_map[7] = 3
        # num_to_count_1s_map[8] = 1
        for i in range(0, len(array)):
            num = array[i]
            num_to_count_1s_map[num] = format(num, 'b').count('1')
        
        count_1s_to_nums_map = {}
        # count_1s_to_nums_map[0] = [0]
        # count_1s_to_nums_map[1] = [1,2,4,8]
        # count_1s_to_nums_map[2] = [3,5,6]
        # count_1s_to_nums_map[3] = [7]

        for num in sorted(array):
            count_1s = num_to_count_1s_map[num]
            if (count_1s in count_1s_to_nums_map.keys()):
                count_1s_to_nums_map[count_1s].append(num)
            else:
                count_1s_to_nums_map[count_1s] = [num]

        ret_val = []
        for count_1s in sorted(count_1s_to_nums_map.keys()):
            ret_val.extend(count_1s_to_nums_map[count_1s])

        return ret_val

array = [0,1,2,3,4,5,6,7,8]
sol = Solution()
sol.sortByBits(array)