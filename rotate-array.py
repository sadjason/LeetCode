# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        start, stop = 0, len(nums)
        
        while start < stop:
            if stop - start <= 1:
                return
            n = stop - start
            k = k % n
            if k == 0:
                return
            for i in xrange(k):
                nums[start+i], nums[stop-k+i] = nums[stop-k+i], nums[start+i]
            start += k