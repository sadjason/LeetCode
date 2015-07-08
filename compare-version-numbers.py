# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        a1, a2 = version1.split('.'), version2.split('.')
        n1, n2 = len(a1), len(a2)
        n = max(n1, n2)

        for i in range(0, n):
            i1 = i2 = 0
            if i < n1:
                i1 = int(a1[i])
            if i < n2:
                i2 = int(a2[i])

            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
            else:
                i += 1
        return 0