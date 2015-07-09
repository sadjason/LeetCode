# encoding: utf-8

__author__ = 'zhangwei'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        # assume root is not None
        cnt = [0]   # 记录已经遍历的结点的个数
        ret = self.aux(root, k, cnt)
        return ret.val
    
    def aux(self, root, k, cnt):    # 中序遍历
        if root.left is not None:
            ret = self.aux(root.left, k, cnt)
            if ret is not None:
                return ret
        cnt[0] += 1
        if cnt[0] == k:
            return root
        if root.right is not None:
            ret = self.aux(root.right, k, cnt)
            if ret is not None:
                return ret