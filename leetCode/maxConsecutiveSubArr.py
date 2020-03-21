def arrayMaxConsecutiveSum2(inputArray):
    dp = []
    dp = [{} for i in range(len(inputArray))]
    dp[0] = inputArray[0]
    for i in range(1, len(inputArray)):
        dp[i] = max(dp[i - 1], 0) + inputArray[i]
    print(dp)
    return max(dp)
