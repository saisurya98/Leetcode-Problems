class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # TC-O(N) iterates through n elements, SC-O(N) Stores a string costs us O(N) space .
        min_len = min(len(word1), len(word2))
        res = ''
        if len(word1) == len(word2):
            for i in range(len(word1)):
                res = res + word1[i] + word2[i]
        elif len(word2) > len(word1):

            for i in range(len(word1)):
                res = res + word1[i] + word2[i]
            res = res + word2[min_len:]
        else:
            for i in range(len(word2)):
                res = res + word1[i] + word2[i]
            res = res + word1[min_len:]
        return res


