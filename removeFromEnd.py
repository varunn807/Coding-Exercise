# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr=temp=head

        for _ in range(n):
            temp=temp.next

        if not temp:
            return head.next

        while temp.next:
            curr=curr.next
            temp=temp.next

        curr.next=curr.next.next

        return head


