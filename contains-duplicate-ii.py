# encoding: utf-8

__author__ = 'zhangwei'

# 使用散列表
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        aDict = dict()

        ret = False

        for j in xrange(len(nums)):
            item = nums[j]
            i = aDict.get(item)
            if i >= 0 and ret is False and j <= i + k:
                if ret is False and j <= i + k:
                    ret = True
                else:
                    return False
            else:
                aDict[item] = j
        return ret