# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        n = len(nums)       # assume n >= 3
        nums.sort()         # sort
        
        ret = nums[0] + nums[1] + nums[2]
        for i in xrange(0, n-2):
            l, r = i+1, n-1
            while l < r:
                sums, t = nums[i] + nums[l] + nums[r], target
                if abs(sums-target) < abs(ret-target):
                    ret = sums
                if sums > target:
                    r -= 1
                elif sums < target:
                    l += 1
                else:
                    return target
        return ret