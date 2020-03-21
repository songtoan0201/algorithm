def productExceptSelf(nums, m):
    N = len(nums)
    output = [{} for i in range(N)]
    output[0] = 1
    for i in range(1, N):
        output[i] = nums[i - 1] * output[i - 1]
    R = 1
    for i in range(N - 1, -1, -1):
        print(i, R)
        output[i] = output[i] * R
        R = R * nums[i]
    # modulo the output arr
    sum = 0
    for i in range(N):
        output[i] = output[i] % m
        sum += output[i]
    return sum % m
    

