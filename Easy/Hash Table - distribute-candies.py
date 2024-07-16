class Solution:
    def distributeCandies(self, candy_types):
        can_eat_only = len(candy_types)//2
        memo = {}
        for candy_type in candy_types:
            if (candy_type in memo.keys()):
                memo[candy_type] += 1
            else:
                memo[candy_type] = 1
        return min(can_eat_only, len(memo.keys()))