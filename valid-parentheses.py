# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        caches = dict((('(',')'), ('{','}'), ('[',']')))
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if caches.has_key(stack[-1]) and  caches[stack[-1]] == c:
                    stack.pop()
                else:
                    stack.append(c)

        if len(stack) == 0:
            return True
        return False