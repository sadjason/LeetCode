# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        ret, cnt = 0, 0
        last = -1
        stack = []      # stack只存储'('
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ret = max(ret, i-last)
                    else:
                        ret = max(ret, i-stack[-1])
                    
        return ret