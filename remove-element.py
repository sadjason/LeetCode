# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        ret = 0
        for item in A:
            if item != elem:
                A[ret] = item
                ret += 1

        return ret