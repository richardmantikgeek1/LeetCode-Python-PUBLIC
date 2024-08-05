class Solution:
    def decode(self, encoded, first):
        decoded = []
        decoded.append(first)
        for i in range(0, len(encoded)):
            decoded.append(first ^ encoded[i])
            first = decoded[i+1]

        return decoded