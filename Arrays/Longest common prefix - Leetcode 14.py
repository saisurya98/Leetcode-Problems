class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs is None or len(strs)==0:
            return ''
        n=len(strs)
        min_str=float('inf')
        output=''
        for i in range(len(strs)):
            if len(strs[i])<min_str:
                min_str=min(min_str,len(strs[i]))
        condition=0
        while condition<min_str:
            myset=set()
            for i in range(len(strs)):
                myset.add(strs[i][condition])
            if len(myset)==1:
                condition+=1
                output+=str(list(myset)[0])
            else:
                return output
        return output
