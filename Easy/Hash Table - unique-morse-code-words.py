class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_code_pattern = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        memo = {}
        for word in words:
            morse_code_encoding = ''.join([morse_code_pattern[ord(c)-97] for c in word])
            memo[morse_code_encoding] = True
        
        return len(memo.keys())