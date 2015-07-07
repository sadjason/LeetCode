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


# 分治法
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1+n2 != n3:
            return False
        return self.aux(s1, 0, s2, 0, s3, 0)

    def aux(self, s1, begin1, s2, begin2, s3, begin3):
        if begin3 == len(s3):
            return True

        if begin1 == len(s1):
            for i in xrange(begin2, len(s2)):
                if s2[i] != s3[begin3-begin2+i]:
                    return False
            return True

        if begin2 == len(s2):
            for i in xrange(begin1, len(s1)):
                if s1[i] != s3[begin3-begin1+i]:
                    return False
            return True

        c1, c2, c3 = s1[begin1], s2[begin2], s3[begin3]
        if c1 != c3 and c2 != c3:
            return False
        elif c1 == c3 and c2 != c3:
            return self.aux(s1, begin1+1, s2, begin2, s3, begin3+1)
        elif c2 == c3 and c1 != c3:
            return self.aux(s1, begin1, s2, begin2+1, s3, begin3+1)
        else:
            b = self.aux(s1, begin1+1, s2, begin2, s3, begin3+1)
            if not b:
                b = self.aux(s1, begin1, s2, begin2+1, s3, begin3+1)
            return b