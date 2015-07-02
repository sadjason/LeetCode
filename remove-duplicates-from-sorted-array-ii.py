# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        tail, cnt = 0, 1
        for i in xrange(1, n):
            if nums[i] != nums[tail]:
                nums[tail+1], tail = nums[i], tail+1
                cnt = 1
            else:
                if cnt < 2:
                    nums[tail+1], tail = nums[i], tail+1
                cnt += 1
                    
        return tail+1