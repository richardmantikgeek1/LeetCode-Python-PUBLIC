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
    def minLength(self, s):
        stack = MyStack()
        i = 0
        while (i < len(s)):
            c = s[i]
            if (not stack.empty()):
                t = stack.top()
                if (t == 'A' and c == 'B') or (t == 'C' and c == 'D'):
                    stack.pop()
                else:
                    stack.push(c)
            else:
                stack.push(c)
            i += 1

        return len(''.join(stack.stack))