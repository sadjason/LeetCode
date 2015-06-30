# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self.aux(nums, 0, len(nums), target)
    
    def aux(self, nums, start, stop, target):
        if stop-start <= 2:
            if nums[start] == target:
                return True
            elif nums[stop-1] == target:
                return True
            else:
                return False
        
        mid = (start + stop) / 2
        if nums[mid] == target:
            return True
        
        if nums[mid] > nums[start]:
            if target >= nums[start] and target < nums[mid]:
                return self.aux(nums, start, mid, target)
            else:
                return self.aux(nums, mid+1, stop, target)
        elif nums[mid] < nums[start]:
            if target <= nums[stop-1] and target > nums[mid]:
                return self.aux(nums, mid+1, stop, target)
            else:
                return self.aux(nums, start, mid, target)
        else:
            if nums[mid] < nums[stop-1]:
                if target > nums[mid] and target <= nums[stop-1]:
                    return self.aux(nums, mid+1, stop, target)
                else:
                    return self.aux(nums, start, mid, target)
            elif nums[mid] > nums[stop-1]:
                return self.aux(nums, mid+1, stop, target)
            else:
                b = self.aux(nums, start, mid, target)
                if not b:
                    b = self.aux(nums, mid+1, stop, target)
                return b