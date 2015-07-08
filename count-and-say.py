# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @return a string
    def countAndSay(self, n):
        result = ''
        if n > 0:
            result = '1'
        for i in range(1, n):
            result = self.aux(result)

        return result
    
    def aux(self, s):
        result = ''
        i = 0
        n = len(s)

        while i < n:
            c = s[i]
            j = i+1
            while j < n:
                temp = s[j]
                if not temp == c:
                    break
                else:
                    j += 1
            result += str(j-i)
            result += c
            i = j

        return result