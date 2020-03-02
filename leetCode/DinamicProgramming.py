def composeRanges(nums):
    result = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if i != j:
            result.append("{}->{}".format(nums[i], nums[j]))
        else:
            result.append(str(nums[j]))
        i = j + 1
    return result

nums: [-1, 0, 1, 2, 6, 7, 9]
Output: ["-1->2", "6->7", "9"]

def houseRobber(A):
    a = b = 0
    for x in A:
        a, b = b + x, max(a, b)
    return max(a, b)


nums: [1, 1, 2, 1]


def mapDecoding(message):
    prev = count = 0
    curr = 1
    
    for i in range(len(message)):
        digit = ord(message[i]) - 48
        number = 0
        if i > 0:
            number = (ord(message[i - 1]) - 48) * 10 + digit
        if digit > 0:
            count = curr
        if number <= 26 and number > 9:
            count += prev
        prev = curr
        curr = count % 1000000007
        count = 0
    return curr

message: "11115112112"
Output: 104