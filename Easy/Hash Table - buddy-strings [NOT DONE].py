from collections import defaultdict

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_map = defaultdict(set)
        for i in range(0, len(s)):
            c = s[i]
            s_map[c].add(i)

        goal_map = defaultdict(set)
        for j in range(0, len(goal)):
            c = goal[j]
            goal_map[c].add(j)
        
        if (sorted(s_map.keys()) != sorted(goal_map.keys())):
            return False
    
        print(s_map)
        print(goal_map)
        indices_diff = []
        for key in sorted(s_map.keys()):
            if (s_map[key] != goal_map[key]):
                indices_diff.append((s_map[key].difference(goal_map[key])))
        
        total_diff = 0
        for i_diff in indices_diff:
            total_diff += i_diff.size()
        if (total_diff % 2 == 0):
            return True
        else:
            return False