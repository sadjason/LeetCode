# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
            
        nums.sort()     # 排序
        
        ret = []
        for i in xrange(0, n-2):
            # 避免重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # two pointers problem
            l, r = i+1, n-1
            while l < r:
                # 去重
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r < n-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                sums, target = nums[l] + nums[r], 0 - nums[i]
                if sums == target:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif sums > target:
                    r -= 1
                else:
                    l += 1
        return ret