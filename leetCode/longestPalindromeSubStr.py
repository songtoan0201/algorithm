class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        length = 0
        start = 0
        end = 0
        for i in range(len(s)):
            lenOddStr = self.expandString(i, i, s)
            lenEvenStr = self.expandString(i, i + 1, s)
            maxLength = max(lenOddStr, lenEvenStr)
            print("max len", maxLength)
            if maxLength > end - start:
                start = i - (maxLength - 1) // 2
                end = i + maxLength // 2

        return s[start: end + 1]

    def expandString(self, left, right, s):
        print(left)
        print(right)
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        print("len", right - left - 1)
        return right - left - 1


n = Solution()

print("Result is", n.longestPalindrome("abad"))
