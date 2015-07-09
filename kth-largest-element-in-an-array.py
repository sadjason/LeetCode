# encoding: utf-8

__author__ = 'zhangwei'


# 最无耻办法 - 两行代码
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[len(nums)-k]