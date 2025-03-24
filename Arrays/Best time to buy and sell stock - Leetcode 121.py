class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low=0
        high=1
        maxp=0
        # 2 pointer approach O(N) TC, O(1) SC
        while high<len(prices):
            print(low,high)
            if prices[low]<prices[high]:
                maxp=max(maxp,prices[high]-prices[low])
            else:
                low=high
            high+=1

        return maxp

