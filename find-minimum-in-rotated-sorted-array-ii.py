# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if len(nums) == 0:
            return 0
        return self.aux(nums, 0, len(nums))
    
    # auxiliary method
    def aux(self, nums, start, stop):
        if stop - start == 1:
            return nums[start]
        elif stop - start == 2:
            return min(nums[start], nums[start+1])

        mid = (start + stop) / 2
        if nums[mid] > nums[stop-1]:
            return self.aux(nums, mid, stop)
        elif nums[mid] == nums[stop-1]:
            if nums[mid] == nums[start]:
                return min(self.aux(nums, start, mid+1), self.aux(nums, mid, stop))
            elif nums[mid] > nums[start]:
                return self.aux(nums, start, mid+1)
        return self.aux(nums, start, mid+1)