# encoding: utf-8

__author__ = 'zhangwei'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        # 计算链表的长度
        n = 0
        node = head
        while node is not None:
            n += 1
            node = node.next
        
        if n == 0:
            return None
        if k % n == 0:
            return head
        
        # 找到第(n-k%n-1)个node和第(n-k%n)个node
        node = head     # 第(n-k%n)个node
        pre = None      # 第(n-k%n-1)个node
        for i in xrange(n-k%n):
            pre = node
            node = node.next
        pre.next = None
        newHead = node
        
        # 找到最后一个node
        tail = newHead
        while tail.next is not None:
            tail = tail.next
        tail.next = head
        return newHead