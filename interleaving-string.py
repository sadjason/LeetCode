# encoding: utf-8

__author__ = 'zhangwei'


# 动态规划
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        m, n, t = len(s1), len(s2), len(s3)
        if t != m+n:
            return False
        if m == t:
            if s1 == s3:
                return True
            return False
        if n == t:
            if s2 == s3:
                return True
            return False

        aux = [[False] * (n+1) for i in xrange(m+1)]
        aux[0][0] = True
        for i in xrange(1, m+1):
            if s1[i-1] == s3[i-1] and aux[i-1][0]:
                aux[i][0] = True
        
        for j in xrange(1, n+1):
            if s2[j-1] == s3[j-1] and aux[0][j-1]:
                aux[0][j] = True
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if aux[i-1][j] and s1[i-1] == s3[i+j-1]:
                    aux[i][j] = True
                elif aux[i][j-1] and s2[j-1] == s3[i+j-1]:
                    aux[i][j] = True
        return aux[m][n]