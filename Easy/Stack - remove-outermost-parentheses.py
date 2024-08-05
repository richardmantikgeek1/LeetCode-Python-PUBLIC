from collections import deque

class MyStack:

    def _init_(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if (not self.empty()):
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        if (not self.empty()):
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def empty(self) -> bool:
        return len(self.stack) == 0
    
class Solution:
    def removeOuterParentheses(self, s):
        i = 0
        parentheses_depth = 0
        ret_val = ''
        while (i < len(s)):
            c = s[i]
            if (c == ')'):
                parentheses_depth -= 1
            if (parentheses_depth >= 1):
                ret_val += c
            if (c == '('):
                parentheses_depth += 1
            i += 1
        
        return ret_val

s = '(()())(())(()(()))'
sol = Solution()
result = sol.removeOuterParentheses(s)
print(result)