
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la,lb=0
        nA,nB=headA,headB

        if headA is None or headB is None:
            return None
        while nA or nB:
            if nA:
                nA=nA.next
                la+=1
            if nB:
                nB=nB.next
                lb+=1

        diff=la-lb
        nA,nB=headA,headB
        if diff>0:
            for _ in range(diff):nA=nA.next
        else:
            for _ in range(abs(diff)): nB = nB.next

        while nA and nB:
            if nA==nB:return nA.val
            nA=nA.next
            nB=nB.next

        return None
