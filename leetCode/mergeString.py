def mergeStrings(s1, s2):
    i = 0
    j = 0
    result = ""
    dict1 = {}
    dict2 = {}
    for ch in s1:
        if ch not in dict1:
            dict1[ch] = 1
        else:
            dict1[ch] += 1
    for ch in s2:
        if ch not in dict2:
            dict2[ch] = 1
        else:
            dict2[ch] += 1
    print(dict1)
    print(dict2)
    while i != len(s1) and j != len(s2):
        if dict1[s1[i]] < dict2[s2[j]]:
            result += s1[i]
            i += 1
        elif dict1[s1[i]] > dict2[s2[j]]:
            result += s2[j]
            j += 1
        elif dict1[s1[i]] == dict2[s2[j]]:
            if s1[i] <= s2[j]:
                result += s1[i]
                i += 1
            else:
                result += s2[j]
                j += 1
    if i <= len(s1) - 1:
        result += s1[i:]
    if j <= len(s2) - 1:
        result += s2[j:]
    return result

s1: "dce"
s2: "cccbd"