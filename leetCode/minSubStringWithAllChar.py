def minSubstringWithAllChars(s, t):
    result = []
    for i in range(len(s)):
        if s[i] in t:
            coll = set()
            for j in range(i, len(s)):
                if s[j] in t:
                    coll.add(s[j])
                    if len(coll) == len(t):
                        result.append(s[i:j+1])
    print(result)
    if result:
        return min(result, key=len)

    return ""
