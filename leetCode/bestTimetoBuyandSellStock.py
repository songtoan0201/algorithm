def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # keep track of the difference between each index
    i = 1
    j = 0
    tempProfit = 0
    while i < len(prices):
        if (prices[i] < prices[j]):
            j = i
        if (prices[i] - prices[j]) > tempProfit:
            tempProfit = prices[i] - prices[j]
        print("i and j", i, j)
        print("cur Profit", tempProfit)
        i += 1
    return tempProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
