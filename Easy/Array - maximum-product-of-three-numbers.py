#User function Template for python3
import numpy as np
class Solution:
    def get_max_pos_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)
        max_pos_num = max(a_list)
        if (max_pos_num > 0):
            return (a_list.index(max_pos_num), max_pos_num)
        else:
            return None
    
    def get_2nd_max_pos_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)

        max_pos_num_tup = self.get_max_pos_num(a_list, len_a_list)
        if (max_pos_num_tup is not None):
            (max_pos_num_index, max_pos_num) = max_pos_num_tup
        else:
            (max_pos_num_index, max_pos_num) = (None, None)

        if (max_pos_num is None):
            return None

        snd_max_pos_num_index = None
        snd_max_pos_num = None
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num > 0 and num <= max_pos_num and num_index != max_pos_num_index):
                if (snd_max_pos_num is None or num > snd_max_pos_num):
                    snd_max_pos_num_index, snd_max_pos_num = num_index, num
        
        if (snd_max_pos_num is not None):
            return (snd_max_pos_num_index, snd_max_pos_num)
        else:
            return None
        
    def get_3rd_max_pos_num(self, a_list, len_a_list):
        max_pos_num_tup = self.get_max_pos_num(a_list, len_a_list)
        if (max_pos_num_tup is not None):
            (max_pos_num_index, max_pos_num) = max_pos_num_tup
        else:
            (max_pos_num_index, max_pos_num) = (None, None)

        snd_max_pos_num_tup = self.get_2nd_max_pos_num(a_list, len_a_list)
        if (snd_max_pos_num_tup is not None):
            (snd_max_pos_num_index, snd_max_pos_num) = snd_max_pos_num_tup
        else:
            (snd_max_pos_num_index, snd_max_pos_num) = (None, None)

        if (max_pos_num is None or snd_max_pos_num is None):
            return None
        
        trd_max_pos_num_index = None
        trd_max_pos_num       = None
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num > 0 
                and num <= snd_max_pos_num 
                and num_index != max_pos_num_index
                and num_index != snd_max_pos_num_index):
                if (trd_max_pos_num is None or num > trd_max_pos_num):
                    trd_max_pos_num_index, trd_max_pos_num = num_index, num
        
        if (trd_max_pos_num is not None):
            return (trd_max_pos_num_index, trd_max_pos_num)
        else:
            return None
    
    def get_min_neg_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)
        min_neg_num = min(a_list)
        if (min_neg_num < 0):
            return (a_list.index(min_neg_num), min_neg_num)
        else:
            return None
    
    

    def get_2nd_min_neg_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)

        min_neg_num_tup = self.get_min_neg_num(a_list, len_a_list)
        if (min_neg_num_tup is not None):
            (min_neg_num_index, min_neg_num) = min_neg_num_tup
        else:
            (min_neg_num_index, min_neg_num) = (None, None)

        if (min_neg_num is None):
            return None


        snd_min_neg_num_index = None
        snd_min_neg_num = None
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num < 0 and num >= min_neg_num and num_index != min_neg_num_index):
                if (snd_min_neg_num is None or num < snd_min_neg_num):
                    snd_min_neg_num_index, snd_min_neg_num = num_index, num
        
        if (snd_min_neg_num is not None):
            return (snd_min_neg_num_index, snd_min_neg_num)
        else:
            return None
        
    
        
    
    # SPECIAL
    def get_max_neg_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)
        try:
            max_neg_num = max([a for a in a_list if a < 0])
            return (a_list.index(max_neg_num), max_neg_num)
        except:
            return None

    def get_2nd_max_neg_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)

        max_neg_num_tup = self.get_max_neg_num(a_list, len_a_list)
        if (max_neg_num_tup is not None):
            (max_neg_num_index, max_neg_num) = max_neg_num_tup
        else:
            (max_neg_num_index, max_neg_num) = (None, None)

        if (max_neg_num is None):
            return None


        snd_max_neg_num_index = None
        snd_max_neg_num = None
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num < 0 and num <= max_neg_num and num_index != max_neg_num_index):
                if (snd_max_neg_num is None or num > snd_max_neg_num):
                    snd_max_neg_num_index, snd_max_neg_num = num_index, num
        
        if (snd_max_neg_num is not None):
            return (snd_max_neg_num_index, snd_max_neg_num)
        else:
            return None
        
    def get_3rd_max_neg_num(self, a_list, len_a_list):
        max_neg_num_tup = self.get_max_neg_num(a_list, len_a_list)
        if (max_neg_num_tup is not None):
            (max_neg_num_index, max_neg_num) = max_neg_num_tup
        else:
            (max_neg_num_index, max_neg_num) = (None, None)

        snd_max_neg_num_tup = self.get_2nd_max_neg_num(a_list, len_a_list)
        if (snd_max_neg_num_tup is not None):
            (snd_max_neg_num_index, snd_max_neg_num) = snd_max_neg_num_tup
        else:
            (snd_max_neg_num_index, snd_max_neg_num) = (None, None)

        if (max_neg_num is None or snd_max_neg_num is None):
            return None
        
        trd_max_neg_num_index = None
        trd_max_neg_num       = None
        
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num < 0 
                and num <= snd_max_neg_num 
                and num_index != max_neg_num_index
                and num_index != snd_max_neg_num_index):
                if (trd_max_neg_num is None or num > trd_max_neg_num):
                    trd_max_neg_num_index = num_index
                    trd_max_neg_num = num      
        if (trd_max_neg_num is not None):
            return (trd_max_neg_num_index, trd_max_neg_num)
        else:
            return None
        
    def get_min_pos_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)
        try:
            min_pos_num = min([a for a in a_list if a > 0])
            return (a_list.index(min_pos_num), min_pos_num)
        except:
            return None
        
    def get_2nd_min_pos_num(self, a_list, len_a_list):
        #len_a_list = len(a_list)

        min_pos_num_tup = self.get_min_pos_num(a_list, len_a_list)
        if (min_pos_num_tup is not None):
            (min_pos_num_index, min_pos_num) = min_pos_num_tup
        else:
            (min_pos_num_index, min_pos_num) = (None, None)

        if (min_pos_num is None):
            return None


        snd_min_pos_num_index = None
        snd_min_pos_num = None
        for num_index in range(0, len_a_list):
            num = a_list[num_index]
            if (num < 0 and num >= min_pos_num and num_index != min_pos_num_index):
                if (snd_min_pos_num is None or num < snd_min_pos_num):
                    snd_min_pos_num_index, snd_min_pos_num = num_index, num
        
        if (snd_min_pos_num is not None):
            return (snd_min_pos_num_index, snd_min_pos_num)
        else:
            return None
    # SPECIAL 
    
        

    def maximumProduct (self, a_list):
        if (len(a_list) < 3):
            return int(np.prod(a_list))

        n = len(a_list)

        max_pos_num_tup         = self.get_max_pos_num(a_list, n)
        snd_max_pos_num_tup     = self.get_2nd_max_pos_num(a_list, n)
        trd_max_pos_num_tup     = self.get_3rd_max_pos_num(a_list, n)

        min_neg_num_tup         = self.get_min_neg_num(a_list, n)
        snd_min_neg_num_tup     = self.get_2nd_min_neg_num(a_list, n)


        max_neg_num_tup         = self.get_max_neg_num(a_list, n)
        snd_max_neg_num_tup     = self.get_2nd_max_neg_num(a_list, n)

        min_pos_num_tup         = self.get_min_pos_num(a_list, n)
        snd_min_pos_num_tup     = self.get_2nd_min_pos_num(a_list, n)

        trd_max_neg_num_tup     = self.get_3rd_max_neg_num(a_list, n)

        
        #print('max_pos_num_tup =', max_pos_num_tup)
        #print('snd_max_pos_num_tup=', snd_max_pos_num_tup)
        #print('trd_max_pos_num_tup=', trd_max_pos_num_tup)
        #print('min_neg_num_tup=',min_neg_num_tup)
        #print('snd_min_neg_num_tup=',snd_min_neg_num_tup)
        #print('max_neg_num_tup=',max_neg_num_tup)
        #print('snd_max_neg_num_tup=',snd_max_neg_num_tup)
        #print('trd_max_neg_num_tup=',trd_max_neg_num_tup)
        #exit(0)

        max_trpl_prod = a_list[0] * a_list[1] * a_list[2]
        # 3 positives
        if (max_pos_num_tup is not None and snd_max_pos_num_tup is not None and trd_max_pos_num_tup is not None):
            max_trpl_prod = max(max_trpl_prod, max_pos_num_tup[1] * snd_max_pos_num_tup[1] * trd_max_pos_num_tup[1])
        
        # 2 negatives, 1 positive
        if (min_neg_num_tup is not None and snd_min_neg_num_tup is not None and max_pos_num_tup is not None):
            max_trpl_prod = max(max_trpl_prod, min_neg_num_tup[1] * snd_min_neg_num_tup[1] * max_pos_num_tup[1])
        
        # any zeros
        try:
            if (a_list.index(0) >= 0):
                max_trpl_prod = max(max_trpl_prod, 0)
        except:
            pass

        # 2 positives, 1 negative
        if (min_pos_num_tup is not None and snd_min_pos_num_tup is not None and max_neg_num_tup is not None):
            max_trpl_prod = max(max_trpl_prod, min_pos_num_tup[1] * snd_min_pos_num_tup[1] * max_neg_num_tup[1])

        # 3 negatives
        if (max_neg_num_tup is not None and snd_max_neg_num_tup is not None and trd_max_neg_num_tup is not None):
            max_trpl_prod = max(max_trpl_prod, max_neg_num_tup[1] * snd_max_neg_num_tup[1] * trd_max_neg_num_tup[1])

        return max_trpl_prod

    def brute_force_max_triplet_prod(self, a_list,  n):
        if (len(a_list) < 3):
            return np.prod(a_list)

        max_trpl_prod = a_list[0] * a_list[1] * a_list[2]
        for i in range(0, len(a_list)):
            num_i = a_list[i]
            for j in range(i+1, len(a_list)):
                num_j = a_list[j]
                for k in range(j+1, len(a_list)):
                    num_k = a_list[k]
                    max_trpl_prod = max(max_trpl_prod, num_i*num_j*num_k)
        
        return max_trpl_prod