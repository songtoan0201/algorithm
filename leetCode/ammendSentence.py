def amendTheSentence(s):
    s = list(s)
    print(s)
    for i,x in enumerate(s):
        if x.isupper():
            s[i] = x.lower()
            if i != 0:
                s[i] = ' ' + s[i]
    return ''.join(s)
        
