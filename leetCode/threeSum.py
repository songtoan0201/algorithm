def threeSum(nums):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    myDict = {}
    arr2D = [[]]
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            #print(nums[i])
            print("i is", i)
            print("j is", j)
            if nums[j] in myDict:
                arr2D.append([i, myDict[nums[j]], j])
            else:
                myDict[-nums[i]] = j
    return arr2D


print( threeSum([-1, 0, 1, 2, -1, -4]))