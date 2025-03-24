class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=set()
        low=0
        count=0
        maxcount=float('-inf')
        for right in range(len(s)):
            while s[right] in myset:
                myset.remove(s[low])
                low+=1
            myset.add(s[right])
            count=(right-low)+1
            maxcount=max(maxcount,count)


        return maxcount

sol=Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))