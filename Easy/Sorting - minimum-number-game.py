class Solution:
    def numberGame(self, array):
        ret_val = []
        alice_min_num_index = None
        bob_min_num_index = None
        step = 0
        while(len(array) >= 2):
            if (step % 2 == 0):
                alice_min_num_index = self.get_min_num_index(array, None)
                bob_min_num_index = self.get_min_num_index(array, alice_min_num_index)
            elif (step % 2 == 1):
                bob_min_num = array[bob_min_num_index]
                ret_val.append(bob_min_num)
                alice_min_num = array[alice_min_num_index]
                ret_val.append(alice_min_num)
                if (alice_min_num_index < bob_min_num_index):
                    array.pop(bob_min_num_index)
                    array.pop(alice_min_num_index)
                else:
                    array.pop(alice_min_num_index)
                    array.pop(bob_min_num_index)
            step += 1
            
        return ret_val

    def get_min_num_index(self, array, excluded_index):
        min_num_index = None
        min_num_value = None
        for i in range(0, len(array)):
            num = array[i]
            if (i == excluded_index):
                continue
            if (min_num_index is None or num < min_num_value):
                min_num_index = i
                min_num_value = num
        
        return min_num_index
    
array = [5,4,2,3]
sol = Solution()
ret_val = sol.numberGame(array)
print(ret_val)