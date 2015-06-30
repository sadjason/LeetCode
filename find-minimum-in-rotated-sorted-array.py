# encoding: utf-8

__author__ = 'zhangwei'

# 递归版本
class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findMin(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        return self.aux(nums, 0, n)
    
    # auxiliary method
    def aux(self, nums, start, stop):
        if stop-start <= 2:
            ret = nums[start]
            if nums[stop-1] < ret:
                ret = nums[stop-1]
            return ret
        
        mid = (start + stop) / 2
        if nums[mid] > nums[stop-1]:
            return self.aux(nums, mid, stop)
        else:
            return self.aux(nums, start, mid+1)


# 迭代版本
class Solution:
    # @param nums, a list of integer
    # @return an integer
    def findMin(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        start, stop = 0, n
        while start < stop:
            if stop - start == 1:   # 只有一个元素，一定是的了
                return nums[start]
            elif stop - start == 2: # 有两个元素，取最小的
                return min(nums[start], nums[start+1])

            mid = (start + stop) / 2
            if nums[mid] > nums[stop-1]:
                start = mid
            else:
                stop = mid+1