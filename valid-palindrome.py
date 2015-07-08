# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        n = len(s)
        l, r = 0, n-1
        while l < r:
            # '0'-'9': 48-57    'a'-'z': 97-122,    'A'-'Z': 65-90
            a1, a2 = ord(s[l]), ord(s[r])
            if a1 < 48 or (a1 > 57 and a1 < 65) or (a1 > 90 and a1 < 97) or a1 > 122:
                l += 1
                continue
            if a2 < 48 or (a2 > 57 and a2 < 65) or (a2 > 90 and a2 < 97) or a2 > 122:
                r -= 1
                continue
            
            t = a1 - a2
            if t == 0 or t == 32 or t == -32:
                l, r = l+1, r-1
            else:
                return False
        return True