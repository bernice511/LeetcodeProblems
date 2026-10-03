class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min = prices[0]
        # profit = 0
        # for i, price in enumerate(prices):
        #     if min>price:
        #         min = price
        #     elif price - min> profit:
        #         profit = price - min
        # return profit
        min = prices[0]
        max_profit = 0
        for price in prices:
            if price<min:
                min = price
            elif price-min>max_profit:
                max_profit = price-min
        return max_profit
            


        