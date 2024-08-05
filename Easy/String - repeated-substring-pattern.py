import math
class Solution:
    def repeatedSubstringPattern(self, s):
        memo = {}
        for c in s:
            if (c in memo.keys()):
                memo[c] += 1
            else:
                memo[c] = 1

        
        count_chars_array = list(memo.values())
        gcd_count_chars = count_chars_array[0]
        i = 1
        while (i < len(count_chars_array)):
            count_repeat = math.gcd(gcd_count_chars, count_chars_array[i])
            i += 1

        if (gcd_count_chars <= 1):
            return False

        count_repeats = self.get_prime_divisors_list(gcd_count_chars)
        for count_repeat in count_repeats:
            len_substring = len(s) // count_repeat

            while(s[:len_substring] * 2 != s[:(len_substring*2)] and len_substring * 2 < len(s)):
                len_substring *= 2
                count_repeat = len(s) // len_substring
            
            if s[:len_substring] * count_repeat == s:
                return True
        
        return False
    
    def get_divisors_list(self, num):
        divisors_list = list()
        if (num != 1):
            for num_i in range (1, num+1):
                if (num % num_i == 0):
                    divisors_list.append(num_i)
        return divisors_list

    def is_prime(self, num):
        for num_1 in range (2, math.floor(math.sqrt(num)) + 1):
            if (num % num_1 == 0):
                return False
        return num != 1 and True

    def get_prime_divisors_list(self, num):
        start_num = 1
        end_num = num

        is_prime_dict = {}
        is_prime_dict[0] = False
        is_prime_dict[1] = False

        for i in range(1, end_num):
            num_i = i+1
            is_prime_dict[num_i] = True

        p = 2
        while (p * p <= end_num):
            # If prime[p] is not
            # changed, then it is a prime
            if (is_prime_dict[p] == True):

                # Update all multiples of p
                for i in range(p * p, end_num+1, p):
                    is_prime_dict[i] = False
            p += 1

        ret_val = []
        for num_i in range(start_num, end_num+1):
            if (is_prime_dict[num_i] and num % num_i == 0):
                ret_val.append(num_i)
        return ret_val
        
s = 'baaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbababaaabbbaba'
sol = Solution()
print(sol.repeatedSubstringPattern(s))