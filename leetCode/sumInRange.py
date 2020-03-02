def sumInRange(nums, queries):
    sum_at = [0] * len(nums)

    total = 0
    for i, x in enumerate(nums):
        total += nums[i]
        sum_at[i] = total

    ans = [0] * len(nums)
    for i, q in enumerate(queries):
        start, end = q[0], q[1]
        if start == 0:
            ans[i] = sum_at[end]
        else:
            ans[i] = sum_at[end] - sum_at[start - 1]

    return sum(ans) % (10**9 + 7)  # read the whole problem!


nums: [3, 0, -2, 6, -3, 2]
queries:
[[0,2], 
 [2,5], 
 [0,5]]