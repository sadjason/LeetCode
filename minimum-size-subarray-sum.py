# encoding: utf-8

__author__ = 'zhangwei'


# 最坏情况，O(2^n)
# Time Limit Exceeded版本
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        n, sums = len(nums), 0
        for i in xrange(n):
            sums += nums[i]

        if n == 0 or sums < s:
            return 0
        return self.aux(nums, sums, 0, n, s)

    def aux(self, nums, sums, start, stop, s):
        if stop - start == 1:
            return 1
        elif start >= stop:
            return 0

        global cnt
        cnt += 1
        if cnt > 20:
            return 0

        print start, stop, sums

        if (sums - nums[start] < s) and (sums - nums[stop-1] < s):
            return stop-start
        elif sums-nums[start] < s:
            return self.aux(nums, sums-nums[stop-1], start, stop-1, s)
        elif sums-nums[stop-1] < s:
            return self.aux(nums, sums-nums[start], start+1, stop, s)
        else:
            c1 = self.aux(nums, sums-nums[stop-1], start, stop-1, s)
            c2 = self.aux(nums, sums-nums[start], start+1, stop, s)
            return min(c1, c2)


# Accepted版本
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        begin, end, sums, ret = 0, 0, 0, 0
        while end < n:
            sums += nums[end]
            while sums >= s:
                if ret == 0 or end-begin+1 < ret:
                    ret = end-begin+1
                sums -= nums[begin]
                begin += 1
            end += 1
                
        return ret