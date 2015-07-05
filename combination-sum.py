# encoding: utf-8

__author__ = 'zhangwei'

# 递归版本
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()   # 排序
        ret, stack = [], []
        self.aux(candidates, 0, ret, stack, target)
        return ret

    # auxiliary method
    def aux(self, candidates, begin, ret, stack, target):
        if target == 0:
            ret.append(stack[::])
            return

        for i in xrange(begin, len(candidates)):
            if candidates[i] <= target:
                stack.append(candidates[i])
                self.aux(candidates, i, ret, stack, target-candidates[i])
                stack.pop()


# 迭代版本
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        down, up = 1, 2		# 分别表示「下探」和「回溯」

        candidates.sort()   # 排序

        stack = [0]
        sums = 0
        pre, dir = 0, down
        ret = []

        while len(stack) > 0:
            cur = stack[-1]
            if dir == down:
                if sums == target:
                    ret.append([candidates[i] for i in stack[1:]])
                    stack.pop()
                    pre, dir, sums = cur, up, sums-candidates[cur]
                elif sums + candidates[cur] <= target:
                    stack.append(cur)
                    pre, dir, sums = cur, down, sums+candidates[cur]
                else:
                    stack.pop()
                    pre, dir, sums = cur, up, sums-candidates[cur]
            else:
                if pre < len(candidates)-1 and sums + candidates[pre+1] <= target:
                    stack.append(pre+1)
                    pre, dir, sums = cur, down, sums+candidates[pre+1]
                else:
                    stack.pop()
                    pre, dir, sums = cur, up, sums-candidates[cur]
        return ret