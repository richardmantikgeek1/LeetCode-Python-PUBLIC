class Solution:
    def restoreString(self, sentence, indices):
        array = ['None'] * len(sentence)
        for i in range(0, len(sentence)):
            array[indices[i]] = sentence[i]
        
        return ''.join(array)