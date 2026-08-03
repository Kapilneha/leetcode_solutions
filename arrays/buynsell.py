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


#method 2
def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))