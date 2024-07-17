class Word:
    def __init__(self, index, char, group):
        self.index = index
        self.char = char
        self.group = group
    
    def __str__(self):
        return '(' + str(self.index) + ', ' + str(self.char) + ', ' + str(self.group) + ')'
import copy
from collections import deque
class Solution:
    def getLongestSubsequence(self, words, groups):
        memo = {}
        for i in range(0, len(words)):
            char = words[i]
            group = groups[i]
            word = Word(i, char, group)

            if (group in memo.keys()):
                memo[group].append(word)
            else:
                memo[group] = deque()
                memo[group].append(word)

        #for k in memo:
        #    words = memo[k]
        #    print(str(k) + ':')
        #    for w in words:
        #        print(w, end=' ')
        
        step = 0
        ret_val_1 = self.get_subseq_starting_with_step(memo, step)

        step = 1
        ret_val_2 = self.get_subseq_starting_with_step(memo, step)
        
        ret_val = None
        if (len(ret_val_1) > len(ret_val_2)):
            ret_val = ret_val_1
        else:
            ret_val = ret_val_2

        return [w.char for w in ret_val]

    def get_subseq_starting_with_step(self, memo, step):
        memo_copy = copy.deepcopy(memo)
        ret_val = []
        last_word = None
        while (step % 2 in memo_copy.keys() and len(memo_copy[step % 2]) > 0):
            words = memo_copy[step % 2]
            if (last_word is not None):
                words_gt_curr_index = deque([w for w in words if w.index > last_word.index])
            else:
                words_gt_curr_index = words
            if (len(words_gt_curr_index) > 0):
                word = words_gt_curr_index.popleft()
                memo_copy[step % 2] = words_gt_curr_index
                ret_val.append(word)
            else:
                break

            last_word = word
            
            step += 1
        
        return ret_val
