class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            if min>price:
                min = price
            elif price - min> profit:
                profit = price - min
        return profit
        