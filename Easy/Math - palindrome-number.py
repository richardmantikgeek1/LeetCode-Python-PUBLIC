class Solution:
    def isPalindrome(self, num):
        num_str = str(num)
        start_index = 0
        while (start_index < len(num_str)):
            c = num_str[start_index]
            last_c = num_str[len(num_str) - start_index - 1]
            if (start_index >= len(num_str) / 2):
                break
                
            if (c != last_c):
                return False
            start_index += 1
        return True