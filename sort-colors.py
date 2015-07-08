# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) == 0:
            return

        C = [0] * 3

        for item in A:
            C[item] += 1

        index = 0
        for i in range(0, 3):
            c = C[i]
            while c > 0:
                A[index] = i
                index += 1
                c -= 1