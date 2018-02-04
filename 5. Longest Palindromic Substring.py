# -*-coding: utf-8 -*-
# Author: 


class Solution:
    # 方法1：
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # 奇数时
            tmp  = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # 偶数时
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    # 方法2：

if __name__ == '__main__':
    s = 'abcddcbe'
    print(Solution().longestPalindrome(s))