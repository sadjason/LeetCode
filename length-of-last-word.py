# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        count = 0
        len_s = len(s)
        for i in range(0, len_s)[::-1]:
            c = s[i]
            if not c == ' ':
                count += 1
            elif count == 0:
                continue
            else:
                break
        return count