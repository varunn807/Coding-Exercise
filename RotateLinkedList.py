# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head


        curr=head
        count=0
        while(curr):
            curr=curr.next
            count+=1
        curr=head
        if k==count or k%count==0:
            return head
        elif k>count:
            k=k%count

        nk=count-k-1
        curr=curr.next
        slow=head
        while nk>0:
            curr=curr.next
            slow=slow.next
            nk-=1

        slow.next=None
        slow=curr
        while curr.next!=None:
            curr=curr.next
        curr.next=head

        return slow




