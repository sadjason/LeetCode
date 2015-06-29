# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        if n == 0:
            return [-1,-1]
        (start, end) = self.aux(nums, 0, n, target)
        return [start, end]
    
    # auxiliary method
    # return (begin, end)
    def aux(self, nums, start, stop, target):
        if stop - start <= 2:
            if nums[start] == target and nums[stop-1] == target:
                return (start, stop-1)
            elif nums[start] == target:
                return (start, start)
            elif nums[stop-1] == target:
                return (stop-1, stop-1)
            else:
                return (-1, -1)
        
        mid = (start + stop) / 2
        if nums[mid] > target:
            return self.aux(nums, start, mid, target)
        elif nums[mid] < target:
            return self.aux(nums, mid+1, stop, target)
        else:
            begin, end = mid, mid
            begin1, end1 = self.aux(nums, start, mid, target)
            if begin1 != -1:
                begin = begin1
            begin2, end2 = self.aux(nums, mid+1, stop, target)
            if begin2 != -1:
                end = end2
            return (begin, end)