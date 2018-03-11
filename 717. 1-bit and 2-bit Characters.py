# -*-coding: utf-8 -*-
# Author: 

"""
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

"""
class Solution:
    def isOneBitCharavter(self, bits):
        """
        :param bits:
        :return:
        """
        if not bits:
            return False
        n = len(bits)
        index = 0
        while index < n:
            if index == n-1:
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False

    # solution 2
    def func(self, bits):
        s = 0
        i = len(bits) - 2
        while bits[i] == 1:
            s += 1
            i -= 1
        return s/2 == s

if __name__ == '__main__':
    s = [1,1,1,1,1]
    print(Solution().isOneBitCharavter(s))
    print(Solution().func(s))