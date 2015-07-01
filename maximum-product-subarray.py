# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        ret = nums[0]
        aux_positive = max(nums[0], 0)
        aux_negative = min(nums[0], 0)

        for i in xrange(1, n):
            if nums[i] == 0:
                aux_positive = aux_negative = 0
            elif nums[i] > 0:
                aux_negative = aux_negative * nums[i]
                aux_positive = max(aux_positive, 1) * nums[i]
            elif nums[i] < 0:
                p, n = aux_positive, aux_negative
                aux_positive = n * nums[i]
                aux_negative = max(p, 1) * nums[i]

            if aux_positive > ret:
                ret = aux_positive

        return ret