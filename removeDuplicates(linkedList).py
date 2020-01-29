# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head
        curr=head
        next=head.next
        result=head
        while next!=None:

            if curr.val==next.val:
                curr.next=next.next
                next=next.next
            else:
                next=next.next
                curr=curr.next
        return result
