# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 0:
            return -1
        return self.aux(nums, 0, n)
        
    # auxiliary method
    def aux(self, nums, start, stop):
        if stop-start <= 2:
            ret = start
            if nums[stop-1] > nums[ret]:
                ret = stop-1
            return ret
        
        mid = (start+stop) / 2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] > nums[mid+1]:
            return self.aux(nums, start, mid)
        else:
            return self.aux(nums, mid+1, stop)


# 迭代版本
class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 0:
            return -1
        start, stop = 0, n
        while start < stop:
            if stop-start <= 2:
                ret = start
                if nums[stop-1] > nums[ret]:
                    ret = stop-1
                return ret
            
            mid = (start+stop) / 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] > nums[mid+1]:
                stop = mid
            else:
                start = mid+1