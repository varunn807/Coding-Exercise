# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head==None or head.next==None:
            return head

        def merge(first,second):
            curr=ListNode(0)
            start=curr

            while(first!=None and second!=None):

                if first.val<second.val:
                    start.next=first
                    first=first.next

                else:
                    start.next = second
                    second = second.next

                start=start.next

            if first:
                start.next=first
            if second:
                start.next=second

            return curr.next





        slow=head
        fast=head.next

        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next

        fast=slow.next
        slow.next=None

        return merge(self.sortList(head),self.sortList(fast))


