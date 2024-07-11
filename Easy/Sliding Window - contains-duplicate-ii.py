class Solution:
    def containsNearbyDuplicate(self, array, k):
        len_array = len(array)
        right_index = 0
        left_index = 0
        a_map = {}
        while left_index < len_array:
            while right_index < len_array:
                r_num = array[right_index]
                if (
                    left_index != right_index
                    and abs(right_index - left_index) <= k
                    and r_num in a_map.keys()
                ):
                    return True
                if right_index - left_index > k:
                    break
                if (r_num in a_map.keys()):
                    a_map[r_num] += 1
                else:
                    a_map[r_num] = 1
                right_index += 1

            if left_index < right_index:
                l_num = array[left_index]
                a_map[l_num]-=1
                if (a_map[l_num] == 0):
                    a_map.pop(l_num)
                left_index += 1
                

        return False

sol = Solution()
print(sol.containsNearbyDuplicate([0,1,2,3,2,5], 3))