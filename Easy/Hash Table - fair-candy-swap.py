class Solution:
    def fairCandySwap(self, alice_candies, bob_candies):
        memo_alice_candies = {}
        for alice_candy in alice_candies:
            memo_alice_candies[alice_candy] = True
        
        memo_bob_candies = {}
        for bob_candy in bob_candies:
            memo_bob_candies[bob_candy] = True

        sum_alice_candies = sum(alice_candies)
        sum_bob_candies = sum(bob_candies)
        same_sum_candies = (sum_alice_candies + sum_bob_candies) // 2
        # sum_bob_candies + alice_candy - bob_candy = same_sum_candies
        # bob_candy = sum_bob_candies + alice_candy - same_sum_candies
        for i in range(0, len(alice_candies)):
            alice_candy = alice_candies[i]
            
            bob_candy = sum_bob_candies + alice_candy - same_sum_candies
            if (bob_candy in memo_bob_candies.keys()):
                return [alice_candy, bob_candy]