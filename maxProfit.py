"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_price = float('inf')
        for idx, price in enumerate(prices):
            if price < min_price:
                min_price = price
            if idx >= 1:
                profit = prices[idx] - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit if max_profit > 0 else 0

Solution().maxProfit([7,6,4,3,1])

