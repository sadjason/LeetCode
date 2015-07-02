# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        tail = 0
        for i in xrange(1, n):
            if nums[i] != nums[tail]:
                nums[tail+1], tail = nums[i], tail+1
        return tail+1