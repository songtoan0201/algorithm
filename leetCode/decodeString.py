def decodeString(s):
    strs = [["", 1]]
    num = 0
    for c in s:
        if c.isdigit():
            # num = num * 10 + ord(c) - 48
            num = num * 10 + int(c)
        elif c == "[":
            strs.append(["", num])
            print(strs)
            num = 0
        elif c == "]":
            sub, cnt = strs.pop()
            print(sub, cnt)
            strs[-1][0] += sub * cnt
        else:
            strs[-1][0] += c
            print(strs)
    return strs[0][0]

s = "2[abc]3[cd]ef"

# String decodeString(String s) {
#     Stack<Integer> intStack = new Stack();
#     Stack<StringBuilder> strStack = new Stack();
#     StringBuilder curr = new StringBuilder();
#     int k = 0;
        
#         for (char ch: s.toCharArray()) {
#             if (Character.isDigit(ch)) {
#                 k = k * 10 + ch - '0';
#             } else if (ch == '[') {
#                 intStack.push(k);
#                 strStack.push(curr);
#                 curr = new StringBuilder();
#                 k = 0;
#             } else if (ch == ']') {
#                 StringBuilder tmp = curr;
#                 curr = strStack.pop();
#                 for(int i = intStack.pop(); i > 0; i--) {
#                     curr.append(tmp);
#                 }
#             } else {
#                 curr.append(ch);
#             }
#         }
#         return curr.toString();
# }
