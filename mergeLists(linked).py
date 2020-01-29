class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head=curr=ListNode(None)

        while l1 or l2:

            if(l1 and l2 == None) or (l1 and l2 and l1.val<=l2.val):
                curr.next=ListNode(l1.val)
                l1=l1.next

            elif l2:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr=curr.next

        return head.next
















