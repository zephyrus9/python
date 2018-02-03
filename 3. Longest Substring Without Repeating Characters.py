# -*-coding: utf-8 -*-
# Author:


class Solution:

    def lengthOfLongestSubstring(self, s):
        """

        :param s:
        :return:
        """
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] +1
            else:
                maxLength = max(maxLength, i -start +1)

            usedChar[s[i]] = i

        return maxLength

if __name__ == '__main__':
    l1 = 'asdfsdfgglhj'
    s = Solution()
    print(s.lengthOfLongestSubstring(l1))
