class Solution:
    # Memory Complexity: O(3) => O(1)
    # Time Complexity: O(N)
    def tribonacci(self, n):
        fib_0 = 0
        fib_1 = 1
        fib_2 = 1
        fib_3 = 2
        i = 0
        while (i < n):
            fib_0 = fib_1
            fib_1 = fib_2
            fib_2 = fib_3
            fib_3 = fib_0 + fib_1 + fib_2

            i += 1

        return fib_0