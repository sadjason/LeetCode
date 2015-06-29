# encoding: utf-8

__author__ = 'zhangwei'

# 递归版本
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        return self.aux(nums, 0, n, target)
    
    # auxiliary method
    def aux(self, nums, start, stop, target):
        if stop-start <= 2:         # 小于等于两个元素
        # 可以拆分为stop-start == 1和stop-start == 2两种情况，逻辑会更清晰一些
            if target <= nums[start]:
                return start
            elif target > nums[stop-1]:
                return stop
            else:
                return stop-1
        
        mid = (start + stop) / 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.aux(nums, start, mid, target)
        else:
            return self.aux(nums, mid+1, stop, target)

# 迭代版本
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0
        start, stop = 0, n
        while start < stop:
            if stop-start <= 2:	# 可以拆分为stop-start == 1和stop-start == 2两种情况，逻辑会更清晰一些
                if target <= nums[start]:
                    return start
                elif target > nums[stop-1]:
                    return stop
                else:
                    return stop-1
            mid = (start+stop) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                stop = mid
            else:
                start = mid+1