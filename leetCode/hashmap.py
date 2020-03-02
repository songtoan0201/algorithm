def hashMap(queryType, query):
    dict = {}

    i = 0
    while i < len(queryType):
        print(i)
        print(dict)
        if queryType[i] == "insert":
            dict[query[i][0]] = query[i][1]
        elif queryType[i] == "addToValue":
            for key in dict:
                dict[key] += query[i][0]
        elif queryType[i] == "addToKey":
            dict = { int(key) + query[i][0] : value for key, value in dict.items() if value }
        elif queryType[i] == "get":
            return dict[query[i][0]]
        i += 1    
    return -1

queryType:
["insert", 
 "addToValue", 
 "get", 
 "insert", 
 "addToKey", 
 "addToValue", 
 "get"]
query:
[[1,2], 
 [2], 
 [1], 
 [2,3], 
 [1], 
 [-1], 
 [3]]