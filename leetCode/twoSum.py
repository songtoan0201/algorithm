def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    myDict = {}
    for i in range(len(nums)):
        #print(nums[i])
        print("i is", i)
        if nums[i] in myDict:
            return [myDict[nums[i]], i]
        else:
            myDict[target-nums[i]] = i
        

print( twoSum([2,7,11,15], 26))
