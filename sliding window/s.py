class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # sliding window variable length
        left=0
        min_len=float('inf')
        sum_index=0
        for right in range(len(nums)):
            sum_index+=nums[right]
            while sum_index>=target:
                min_len=min(min_len,right-left+1)
                sum_index-=nums[left]
                left+=1
        return min_len if min_len!=float('inf') else 0
sol = Solution()
print(sol.minSubArrayLen(7,[2,3,1,2,4,3]))