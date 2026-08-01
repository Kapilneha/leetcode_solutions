def maxProfit(prices):

    mini = float('inf')
    profit = 0

    for price in prices:

        if price < mini:
            mini = price

        elif price - mini > profit:
            profit = price - mini

    return profit


prices = list(map(int, input("Enter stock prices: ").split()))

print("Maximum Profit:", maxProfit(prices))