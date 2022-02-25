class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_hold, dp_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = dp_hold, dp_not_hold
            
            # either keep not hold, or sell out today at stock price
            dp_not_hold = max(prev_not_hold, prev_hold + stock_price)
            
            # either keep hold, or buy in today at stock price and pay transaction fee for this trade
            dp_hold = max(prev_hold, prev_not_hold - stock_price - fee)
        
        # maximum profit must be in not-hold state
        return dp_not_hold