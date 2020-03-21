def textJustification(words, L):
    sol = [] 
    while words:
        sol.append('')
        while words and L - len(sol[-1]) >= len(words[0]):
            sol[-1] += words.pop(0) + ' '
        sol[-1] = sol[-1][:-1]
    for i, lineWord in enumerate(sol):
        l1 = L - len(lineWord)
        spaceCount = lineWord.count(' ')
        if i == len(sol) - 1 or not spaceCount:
            sol[i] = sol[i] + ' ' * l1
        else:
            k = l1 // spaceCount
            sol[i] = sol[i].replace(' ', ' ' * (k + 1))
            sol[i] = sol[i].replace(' ' * (k + 1), ' ' * (k + 2), l1 % spaceCount)
    return sol

words:
["This",
 "is",
 "an",
 "example",
 "of",
 "text",
 "justification."]
l: 16
