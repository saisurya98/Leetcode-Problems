class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index1,index2=0,0
        while index1<len(s) and index2<len(t):

            if s[index1]==t[index2]:
                index1+=1
                index2+=1
            elif s[index1]!=t[index2]:
                index2+=1
        return True if index1==len(s) else False
