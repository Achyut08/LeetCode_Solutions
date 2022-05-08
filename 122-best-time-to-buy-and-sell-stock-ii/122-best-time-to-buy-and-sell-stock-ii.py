class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #This is the max total profit we can make from the prices array
        profit = 0
        
        #We iterate through the prices array starting at 1
        for i in range(1, len(prices)):
            #If the current price is larger than the previous value, that mean's we're going
            #to sell it
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        #We return the profit
        return profit