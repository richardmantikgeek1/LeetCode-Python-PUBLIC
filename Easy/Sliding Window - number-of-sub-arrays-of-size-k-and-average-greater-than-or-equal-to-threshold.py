class Solution:
    def numOfSubarrays(self, array, k, threshold):
        len_array = len(array)
        start_index = 0
        end_index = start_index + k - 1
        ret_val = 0
        sum_subarray = sum(array[start_index:end_index+1])
        while (end_index < len_array):
            if (sum_subarray/k >= threshold):
                ret_val += 1
            sum_subarray -= array[start_index]
            start_index += 1
            end_index = start_index + k - 1
            try:
                sum_subarray += array[end_index]
            except:
                pass
        return ret_val