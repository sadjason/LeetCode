# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        ret, stack = [], []
        self.aux(1, ret, stack, k, n)
        return ret
        
    def aux(self, begin, ret, stack, cnt, target):
        if target == 0 and len(stack) == cnt:
            ret.append(stack[::])
            return
        
        for i in xrange(begin, 10):
            if len(stack) < cnt and i <= target:
                stack.append(i)
                self.aux(i+1, ret, stack, cnt, target-i)
                stack.pop()

# 迭代版本
class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        stack = []
        sums = 0
        stack.append(0)
        down, up = 1, 2
        pre, dir = 0, down
        ret = []
        
        while len(stack) > 0:
            cur = stack[-1]
            stackSize = len(stack)
            if dir == down:
                if stackSize-1 < k and cur < 9 and sums + (cur+1) <= n:
                    stack.append(cur+1)
                    pre, dir, sums = cur, down, sums+cur+1
                else:
                    if stackSize-1 == k and sums == n:
                        ret.append(stack[1::])
                    stack.pop()
                    pre, dir, sums = cur, up, sums-cur
            else:
                if pre < 9 and sums+(pre+1) <= n:
                    stack.append(pre+1)
                    pre, dir, sums = cur, down, sums+pre+1
                else:
                    stack.pop()
                    pre, dir, sums = cur, up, sums-cur
        return ret