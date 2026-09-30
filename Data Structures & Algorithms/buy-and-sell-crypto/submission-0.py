class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        ans=0
        for j in range(1,len(prices)):
            if prices[i]>prices[j]:
                i=j
            else:
                ans=max(ans,prices[j]-prices[i])
        return ans 