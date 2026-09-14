class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 # left: buy and right : sell
        maxP = 0

        while r < len(prices): # iter through the whole list
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP

                


        
        