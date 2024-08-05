from collections import deque

class MyStack:

    def __init__(self):
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
    def maxDepth(self, s):
        i = 0
        parentheses_depth = 0
        max_parentheses_depth = 0
        while (i < len(s)):
            c = s[i]
            if (c == '('):
                parentheses_depth += 1
                max_parentheses_depth = max(parentheses_depth, max_parentheses_depth)
            elif (c == ')'):
                parentheses_depth -= 1
            i += 1

        return max_parentheses_depth

s = '(1+(2*3)+((8)/4))+1'
sol = Solution()
result = sol.maxDepth(s)
print(result)