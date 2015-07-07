# encoding: utf-8

__author__ = 'zhangwei'


# 递归版本
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        ret, stack = [], []
        self.aux(ret, stack, 0, 0, n)
        return ret
    
    def aux(self, results, stack, lefts, rights, n):
    	# lefts和rights分别记录stack中'('和')'的个数
        if lefts + rights == 2 * n:
            results.append(''.join(stack))
            return
        
        if lefts < n and lefts == rights:
            stack.append('(')
            self.aux(results, stack, lefts+1, rights, n)
            stack.pop()
        elif lefts == n and lefts > rights:
            stack.append(')')
            self.aux(results, stack, lefts, rights+1, n)
            stack.pop()
        elif lefts < n and lefts > rights:
            stack.append('(')
            self.aux(results, stack, lefts+1, rights, n)
            stack.pop()
            stack.append(')')
            self.aux(results, stack, lefts, rights+1, n)
            stack.pop()


# 迭代版本
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n <= 0:
            return ['']
        
        ret = []
        stack = [''] * (2 * n)
        stack[0] = '('              # 左括号入栈
        stackSize = 1               # 为避免没必要的push和pop操作，stackSize用于记录「栈」信息
        lefts, rights = 1, 0        # 分别记录已入栈的左括号和右括号的数量
        
        down, up = 1, 2             # 分别表示「下探」和「回溯」
        pre, dir = 0, down          # pre记录上一个处理（或压栈、或弹出）的结点，dir记录方向
        
        while stackSize > 0:
            cur = stack[stackSize-1]
            if stackSize == 2*n:    # 已有2n个结点入栈
                ret.append("".join(stack))
                stackSize, pre, dir, rights = stackSize-1, cur, up, rights-1
                continue
            
            if dir == down:
                if lefts < n:
                    stack[stackSize] = '('
                    stackSize, pre, dir, lefts = stackSize+1, cur, down, lefts+1
                else:
                    stack[stackSize] = ')'
                    stackSize, pre, dir, rights = stackSize+1, cur, down, rights+1
            else:
                if pre is '(' and lefts > rights:
                    stack[stackSize] = ')'
                    stackSize, pre, dir, rights = stackSize+1, cur, down, rights+1
                elif cur is '(':
                    stackSize, pre, dir, lefts = stackSize-1, cur, up, lefts-1
                elif cur is ')':
                    stackSize, pre, dir, rights = stackSize-1, cur, up, rights-1
        return ret