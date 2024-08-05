class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        temp_1 = [a for a in letters if a > target]
        if (len(temp_1) > 0):
            return min(temp_1)
        else:
            temp_2 = [a for a in letters]
            return min(temp_2)