class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set max profit to 0
        max_profit=0
        #set min price to the first price in the prices array
        min_price=prices[0]
        
        #loop from the second price in the array since first price is captured in min_price
        for i in range(1,len(prices)): 
            #update min_price
            min_price=min(min_price, prices[i])
            #updte max profit
            max_profit=max(max_profit,prices[i]-min_price)  
        return max_profit