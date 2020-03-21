def findLongestSubarrayBySum(s, arr):
    total = j = 0
    res = (0,-1)
    for i, value in enumerate(arr):
        total += value
        # continue adding value 
        while j<=i and total>s:
            # subtract value that make larger than total
            total -= arr[j]
            j += 1
        print(total, i, j)
        if (total == s) and (res[1]-res[0]<i-j):
            res=(j+1,i+1)
    return res if res[0] else [-1]
            
        
