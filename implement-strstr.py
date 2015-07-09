# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # haystack - 被查找的字符串，needle - 匹配字符串
        m, n = len(needle), len(haystack)

        for i in xrange(0, n-m+1):
            flag = True
            for j in xrange(0, m):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1