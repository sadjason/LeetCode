# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()   # 排序
        ret, stack = [], []
        self.aux(candidates, 0, ret, stack, target)
        return ret
    
    def aux(self, candidates, begin, ret, stack, target):
        if target == 0:
            ret.append([candidates[i] for i in stack])
            return
        
        for i in xrange(begin, len(candidates)):
            if candidates[i] <= target:
                if i > 0 and candidates[i] == candidates[i-1]:
                    if len(stack) > 0 and stack[-1] == i-1:
                        stack.append(i)
                        self.aux(candidates, i+1, ret, stack, target-candidates[i])
                        stack.pop()
                else:
                    stack.append(i)
                    self.aux(candidates, i+1, ret, stack, target-candidates[i])
                    stack.pop()


# 迭代版本
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        
        candidates.sort()   # 排序
        n = len(candidates)

        stack = []          # 记录被选中的item的index
        sums = 0            # 记录被选中的元素们的和
        down, up = 1, 2     # 分别表示「下探」和「回溯」
        stack.append(False) # 根节点（根节点的值无意义）
        pre, dir = 0, down  # pre - 记录上一个处理的「结点」，dir - 方向
        ret = []

        while len(stack) > 0:
            cur, stackSize = stack[-1], len(stack)
            if dir == down:
                if sums == target and stackSize-1 == n:
                    ret.append([candidates[i-1] for i in xrange(1,stackSize) if stack[i]])
                    stack.pop()
                    pre, dir = cur, up
                    if cur:
                        sums -= candidates[stackSize-2]
                elif sums == target:
                    stack.append(False)
                    pre, dir = cur, down
                elif stackSize > 1 and stackSize-1 < n and candidates[stackSize-2] == candidates[stackSize-1] and not cur:
                    stack.append(False)
                    pre, dir = cur, down
                elif stackSize-1 < n and sums + candidates[stackSize-1] <= target:
                    stack.append(True)
                    pre, dir, sums = cur, down, sums+candidates[stackSize-1]
                else:
                    stack.pop()
                    pre, dir = cur, up
                    if cur:
                        sums -= candidates[stackSize-2]
            else:
                if pre:
                    stack.append(False)
                    pre, dir = cur, down
                else:
                    stack.pop()
                    pre, dir = cur, up
                    if cur:
                        sums -= candidates[stackSize-2]
        return ret