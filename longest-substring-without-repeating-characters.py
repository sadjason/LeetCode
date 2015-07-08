# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0

        caches = dict()
        begin, end, ret = 0, 0, 1
        while end < n:
            if s[end] not in caches:
                caches[s[end]] = end
                ret = max(end-begin+1, ret)
            else:
                for i in xrange(begin, caches[s[end]]):
                    caches.pop(s[i])
                begin = caches[s[end]] + 1
                caches[s[end]] = end
            end += 1
        return ret