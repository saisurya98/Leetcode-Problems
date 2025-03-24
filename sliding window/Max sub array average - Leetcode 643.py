class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        maxavg = float('-inf')
        # 1+12-5-6
        low = 0
        sum_i = 0
        # intial avg sum of of first valid window -global variable
        for i in range(k):
            sum_i += nums[i]
        maxavg = max(maxavg, sum_i / k)

        # compute sum of rest of valid windows
        for i in range(k, len(nums)):
            sum_i = sum_i + nums[i]
            sum_i = sum_i - nums[i - k]
            maxavg = max(maxavg, sum_i / k)
        return maxavg


sol=Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3],4))
