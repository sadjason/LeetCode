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
        
        for i in xrange(0, n-1):
            j = binary_search(nums, target-nums[i], i+1, n)
            if j != -1:
                return (min(indexs[i]+1, indexs[j]+1), max(indexs[i]+1, indexs[j]+1))
        return (0, 0)
            

def binary_search(A, target, start, stop):
    if start >= stop:
        return -1
    
    while start < stop:
        if stop - start <= 2:
            if target == A[start]:
                return start
            elif target == A[stop-1]:
                return stop-1
            else:
                return -1
        mid = (start+stop) / 2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            stop = mid
        else:
            start = mid+1
        
        
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