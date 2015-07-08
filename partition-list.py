# encoding: utf-8

__author__ = 'zhangwei'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        # 定义两个链表，前者中的node的val值都小于x，后者的node的val值大于或等于x
        fakeHead1 = ListNode(0)
        fakeHead2 = ListNode(0)
        tail1, tail2 = fakeHead1, fakeHead2
        node = head
        while node is not None:
            if node.val < x:
                tail1.next = node
                tail1 = node
            else:
                tail2.next = node
                tail2 = node
            node = node.next
        
        tail2.next = None
        tail1.next = fakeHead2.next
        return fakeHead1.next