# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        n = len(nums)
        if len(nums) == 0:
            return 0
        
        ret = aux = nums[0]
        # ret：返回值；aux：记录以nums[i]为末尾元素的最大子数组和
        for i in xrange(1, n):
            if aux > 0:
                aux += nums[i]
            else:
                aux = nums[i]
            if aux > ret:
                ret = aux
        return ret