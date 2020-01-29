# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        val=0
        root=result=ListNode(0)
        while l1 or l2 or carry:
            if not l1 and not l2:
                sum=carry
            elif not l1:
                sum=l2.val+carry
                l2=l2.next
            elif not l2:
                sum=l1.val+carry
                l1=l1.next

            else:
                sum=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
            #print(sum)
            if sum>=10:
                carry=1
                val=sum%10
                #print(val)
            else:
                val=sum
                carry=0
            #print(val)

            result.next=ListNode(val)
            result=result.next

        return root.next


l1=ListNode(5)

# l=ListNode(4)
# l1.next=l
#
# c=ListNode(3)
# l.next=c

l2=ListNode(5)

# l=ListNode(6)
# l2.next=l
#
# c=ListNode(4)
# l.next=c

sol=Solution()
res=sol.addTwoNumbers(l1,l2)

while res!=None:
    print(res.val)
    res=res.next