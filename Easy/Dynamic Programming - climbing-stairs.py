class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_stairs(n)

    def climb_stairs(self, n: int):
        fib_nums = [None, 1, 2]
        if (n < len(fib_nums)):
            return fib_nums[n]
        fib_num_1 = 1
        fib_num_2 = 2
        fib_num_3 = 3
        i = 3
        while (i < n):
            fib_num_1 = fib_num_2
            fib_num_2 = fib_num_3
            fib_num_3 = fib_num_1 + fib_num_2

            i += 1
        return fib_num_3

    def brute_force_climb_stairs(self, n):
        steps_list = []
        ret_val = 0
        if (steps_list == []):
            if (1 <= n):
                steps_list.append(1)
            if (2 <= n):
                steps_list.append(2)
        
            while (len(steps_list) > 0):
                steps = steps_list.pop(0)
                if (steps == n):
                    ret_val+=1
                if (steps + 1 <= n):
                    steps_list.append(steps + 1)
                if (steps + 2 <= n):
                    steps_list.append(steps + 2)
        return ret_val
    
for N in range(1,10):
    res = Solution().climbStairs(N)
    print(N, res)
    res2 = Solution().brute_force_climb_stairs(N)
    print(N, res2)