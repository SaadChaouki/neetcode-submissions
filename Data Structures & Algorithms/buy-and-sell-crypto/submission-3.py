class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We have a list of prices where we need to choose a day when to buy 
        # and a day when to sell. The day when to sell cannot be in the past.
        # Essentially, what we need to do is find the lowest value then find 
        # the max value after that index. 

        # Creating variables to hold the buy and the sell price. We buy directly 
        # the first day.
        buy_price: int = prices[0]
        sell_price: int | None = None
        max_profit_seen: int = 0

        # What we need to do is essentially go through the list once, keep track
        # of the lowest price we find.

        for idx, price in enumerate(prices[1:]):
            
            # IF there's a new better price, let's buy and reset the sell price.
            if price < buy_price and idx < len(prices) - 2:
                buy_price = price
                sell_price = None
            
            # If there's a good sell price, we sell. 
            elif sell_price is None and price > buy_price:
                sell_price = price
                max_profit_seen = max(max_profit_seen, sell_price - buy_price)

            # If there's a better sell price, we sell
            elif sell_price is not None and (price - buy_price) > (sell_price - buy_price) :
                sell_price = price
                max_profit_seen = max(max_profit_seen, sell_price - buy_price)

        
        return max_profit_seen

            

