# encoding: utf-8

__author__ = 'zhangwei'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, nums, target):
        n = len(nums)
        if n < 2:
            return (0, 0)
        indexs = [i for i in xrange(n)]	# 记录位置
        quick_sort(nums, indexs, 0, n)  # 排序

        # Two Pointers处理
        i, j = 0, n-1
        while i < j:
            sums = nums[i] + nums[j]
            if sums == target:
                return (min(indexs[i]+1, indexs[j]+1), max(indexs[i]+1, indexs[j]+1))
            elif sums > target:
                j -= 1
            else:
                i += 1

        return (0, 0)

        
# 快速排序
def quick_sort(A, indexs, start, stop):
    if stop - start < 2:
        return

    # 随机化reference
    mid = (start + stop) / 2
    A[mid], A[stop-1] = A[stop-1], A[mid]
    indexs[mid], indexs[stop-1] = indexs[stop-1], indexs[mid]

    # partition
    p = start
    for i in xrange(start, stop-1):
        if A[i] < A[stop-1]:
            A[p], A[i] = A[i], A[p]
            indexs[p], indexs[i] = indexs[i], indexs[p]
            p += 1
    A[stop-1], A[p] = A[p], A[stop-1]
    indexs[stop-1], indexs[p] = indexs[p], indexs[stop-1]
    # p左侧元素都小于A[p]，右侧的元素都大于等于A[p]

    # divide and conquer
    quick_sort(A, indexs, start, p)
    quick_sort(A, indexs, p+1, stop)