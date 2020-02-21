def findSubstrings(words, parts):
    dict = {}
    for str in parts:
        dict[str] = True
    for i in range(len(words)):
        length = len(words[i])
        j = length
        while j > 0:
            for k in range(0, length - j + 1):
                print("k: ", k)
                substr = words[i][k:(k + j)]
                print(substr)
                if substr in dict:
                    words[i] = words[i].replace(substr, "[" + substr + "]", 1)
                    j = 0
                    break
            j -= 1

    return words


words:
["Apple",
 "Melon",
 "Orange",
 "Watermelon"]
parts:
["a",
 "mel",
 "lon",
 "el",
 "An"]
