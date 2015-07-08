# encoding: utf-8

__author__ = 'zhangwei'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        
        # 计算链表的的长度
        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next

        # 获取要删除的node的index，从0开始
        targetIndex = listLen - n

        index = 0
        node = head
        pre = None
        while index != targetIndex:
            pre = node
            node = node.next
            index += 1
        
        if pre is None:     # targetIndex == 0
            return head.next
        else:
            pre.next = node.next
        return head