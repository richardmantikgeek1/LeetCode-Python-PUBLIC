from collections import defaultdict

class Solution:
    def shortestCompletingWord(self, license_plate, words):
        all_letters_in_license_plate = defaultdict(bool)
        for l in license_plate:
            if l.isalpha():
                all_letters_in_license_plate[l.lower()]+= 1
        
        count_chars_to_completing_word_map = defaultdict(list)
        for word in words:
            all_letters_in_word = defaultdict(bool)
            for c in word:
                all_letters_in_word[c.lower()]+=1
            
            is_completing_word = True
            for l in all_letters_in_license_plate.keys():
                if (l not in all_letters_in_word.keys()
                    or all_letters_in_license_plate[l] > all_letters_in_word[l]):
                    is_completing_word = False
            if (is_completing_word):
                count_chars_to_completing_word_map[len(word)].append(word)
        
        for count_chars in sorted(count_chars_to_completing_word_map.keys()):
            return count_chars_to_completing_word_map[count_chars][0]

license_plate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
sol = Solution()
result = sol.shortestCompletingWord(license_plate, words)
print(result)