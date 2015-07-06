# encoding: utf-8

__author__ = 'zhangwei'


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        n = len(intervals)
        if n == 0:
            return [newInterval]
        starts = [interval.start for interval in intervals]
        starts.append(newInterval.start)
        ends = [interval.end for interval in intervals]
        ends.append(newInterval.end)
        starts.sort()
        ends.sort()
        results = []
        
        i = 0
        while i <= n:
            j = i
            while j < n and ends[j] >= starts[j+1]:
                j += 1
            results.append(Interval(s=starts[i], e=ends[j]))
            i = j+1
        return results