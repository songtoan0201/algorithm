def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    newStr = ""
    count = 1
    if (len(n) == 1):
        return str(count) + n
    for i in range (1, len(n)):
        if n[i] == n[i-1]:
            count += 1
        else:
            newStr += str(count) + n[i-1]
            count = 1

    newStr += str(count) + n[i]
            
    return newStr


print(countAndSay("22234"))
    
    