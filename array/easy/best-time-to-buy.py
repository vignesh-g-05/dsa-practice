"""
121. Best Time to Buy and Sell Stock

Brute Force:
Check all pairs (buy, sell)
Time: O(n**2)
Space: O(1)

Optimal:
Track minimum price so far and compute max profit
Time: O(n)
Space: O(1)
"""


def approach1(prices: list[int]) -> int:
    max = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            curr_price = prices[j] - prices[i]
            if curr_price > max:
                max = curr_price

    return max


def approach2(prices: list[int]) -> int:
    min_invest = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_invest
        if profit > max_profit:
            max_profit = profit

        if prices[i] < min_invest:
            min_invest = prices[i]

    return max_profit
