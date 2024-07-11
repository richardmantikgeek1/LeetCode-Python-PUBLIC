class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_index = 0

        while (len(needle) <= len(haystack)):
            if (haystack.startswith(needle)):
                return start_index
            start_index += 1
            haystack = haystack[1:]

        return -1
    
sol = Solution()
print(sol.strStr('hello', 'll'))