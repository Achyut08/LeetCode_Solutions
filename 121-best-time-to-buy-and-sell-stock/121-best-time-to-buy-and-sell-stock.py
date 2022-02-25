class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lst = float(inf) #least so far
        profit = 0
        psit = 0 #profit if soild today
        lst = prices[0]
        for i in range(1,len(prices)):
            if (prices[i] < lst):
                lst = prices[i]
                print(lst)
            psit = prices[i] - lst
            print(psit)
            if (psit > profit):
                profit = psit
            # print(lst, profit)
        return profit
        
#         if len(prices) == 0:
#             return 0
#         else:
#             max_profit = 0
#             min_price = prices[0]
#             for i in range(len(prices)):
#                 profit = prices[i] - min_price   # yaha bech(sell) kar rahe hai
#                 max_profit = max(profit, max_profit)
#                 min_price = min(min_price, prices[i])

#             return max_profit
       
        
        