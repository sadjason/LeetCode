# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        stop = 0
        for i in range(0, len(strs[0])):
            testChar = strs[0][i]
            for j in range(1, len(strs)):
                str = strs[j]
                if len(str) <= i or str[i] != testChar:
                    return strs[0][:stop]
            stop += 1
        return strs[0][:stop]