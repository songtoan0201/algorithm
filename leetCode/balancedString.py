def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    countL = 0
    countR = 0
    result = 0
    for i in range(len(s)):
        if (s[i] == "L"):
            countL += 1
        elif (s[i] == "R"):
            countR += 1
        if countL == countR:
            result += 1
            countL = 0
            countR = 0
    return result

print( balancedStringSplit("RLLLLRRRLR"))