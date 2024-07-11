class Solution:
    def minOperations(self, array):
        len_array = len(array)
        count_operations = 0
        sorted_array = [array[0]] * len(array)
        i = 0
        while(i < len_array-1):
            sorted_array[i] = array[i]
            if (array[i] < array[i+1]):
                i += 1
            else:
                break
        else:
            sorted_array[i] = array[i]

        while (i < len_array-1):
            if (array[i+1] <= sorted_array[i]):
                sorted_array[i+1] = sorted_array[i] + 1
            else:
                sorted_array[i+1] = array[i+1]

            i+=1
        #print(sorted_array, i)

        for i in range(0, len_array):
            count_operations += sorted_array[i] - array[i]

        return count_operations

    def minOperations_2(self, array):
        count_operations = 0
        is_sorted = False
        while (not is_sorted):
            is_sorted = True
            for i in range(len(array)-1,0,-1):
                j = i - 1
                if (array[j] < array[i]):
                    continue
                else:
                    array[i] += 1
                    count_operations += 1
                    is_sorted = False
        
        return count_operations
    
sol = Solution()
print(sol.minOperations([4881,2593,6819,9256,4135]))