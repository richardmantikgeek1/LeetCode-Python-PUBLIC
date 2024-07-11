class Solution:
    def findKOr(self, array, k):
        max_num = max(array)
        binary_max_num = format(max_num, 'b')
        len_bits = len(binary_max_num)

        binary_result = ''

        i = len_bits - 1
        bits = []
        while (i >= 0):
            for j in range(0, len(array)):
                num = array[j]
                binary_num = format(num, 'b').zfill(len_bits)
                bits.append(binary_num[i])
            if (len([b for b in bits if b == '1']) >= k):
                binary_result = '1' + binary_result
            else:
                binary_result = '0' + binary_result
            #print(bits, binary_result)
            #input()
            i -= 1
            bits = []
        
        return int(binary_result, 2)
        

array = [7,12,9,8,9,15]
k = 4
sol = Solution()
result = sol.findKOr(array, k)
print(result)