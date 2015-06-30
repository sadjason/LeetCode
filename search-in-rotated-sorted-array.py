# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self.aux(nums, 0, len(nums), target)
    
    def aux(self, nums, start, stop, target):
        if stop-start <= 2:
            if nums[start] == target:
                return start
            elif nums[stop-1] == target:
                return stop-1
            else:
                return -1
        
        mid = (start + stop) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[mid] > nums[stop-1] and target <= nums[stop-1]:
                return self.aux(nums, mid+1, stop, target)
            else:
                return self.aux(nums, start, mid, target)
        else:
            if nums[mid] < nums[start] and target > nums[stop-1]:
                return self.aux(nums, start, mid, target)
            else:
                return self.aux(nums, mid+1, stop, target)