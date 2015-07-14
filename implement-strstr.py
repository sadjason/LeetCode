# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # haystack - 文本串，needle - 模式串
        m, n = len(haystack), len(needle)

        for i in xrange(0, m-n+1):
            flag = True
            for j in xrange(0, n):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1


# KMP算法
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        # haystack - 文本串，needle - 模式串
        m, n = len(haystack), len(needle)

        # 计算next
        next = self.calNext(needle)

        i = j = 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
            else:   # find k and update j
                if next[j] == -1:
                    i, j = i+1, 0
                else:
                    j = next[j]

        if j == n:
            return i-n
        return -1

    def calNext(self, pattern):     # pattern - 模式串
        n = len(pattern)
        next = [-1] * n
        j, k = 0, -1    # j, k = 0, next[0]
        while j < n-1:
            if k == -1 or pattern[k] == pattern[j]:
                j, k = j+1, k+1
                #next[j] = k
                if pattern[j] == pattern[k]:
                    next[j] = next[k]
                else:
                    next[j] = k
            else:
                k = next[k]
        return next
