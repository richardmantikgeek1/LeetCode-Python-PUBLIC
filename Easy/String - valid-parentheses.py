class Solution:
    def isValid(self, S):
        start_index = 0
        stack = []
        while(start_index < len(S)):
            c = S[start_index]
            if (c == '('):
                stack.append(c)
            elif (c == '['):
                stack.append(c)
            elif (c == '{'):
                stack.append(c)
            elif (c == ')'):
                try:
                    c0 = stack.pop()
                    if (c0 != '('):
                        return False
                except:
                    return False

            elif (c == ']'):
                try:
                    c0 = stack.pop()
                    if (c0 != '['):
                        return False
                except:
                    return False
                
            elif (c == '}'):
                try:
                    c0 = stack.pop()
                    if (c0 != '{'):
                        return False
                except:
                    return False

            start_index += 1

        return len(stack) == 0
    
sol = Solution()
print(sol.isValid('(]'))