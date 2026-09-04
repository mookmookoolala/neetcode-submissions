class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = {}
        j = 0
        for l in range(len(prices)):
            for m in range(l+1, len(prices)):
                if prices[m] > prices[l]:
                    j = max(j, prices[m]-prices[l])
        return j
