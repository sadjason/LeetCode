# encoding: utf-8

__author__ = 'zhangwei'


# based on bit manipulation
class Solution:
    # @param nums, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        negatives = 0           # 记录负数个数
        buf = [0] * 32          # 记录位
        for item in nums:
            if item < 0:
                negatives += 1
                item = abs(item)
            for i in xrange(32):
                if item % 2 == 1:
                    buf[31-i] += 1
                item /= 2

        half = (n+1) / 2
        ret = 0
        mul = 1
        for i in xrange(32):
            if buf[31-i] >= half:
                ret += mul
            mul *= 2
        if negatives >= half:
            ret = 0-ret

        return ret


# smarter one
class Solution:
    # @param nums, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        ret, count = 0, 0
        for num in nums:
            if count == 0:
                ret = num
                count += 1
            elif num == ret:
                count += 1
            else:
                count -= 1
        return ret