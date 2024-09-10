# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        current = head

        while current.next:
            gcd = find_gcd(current.val, current.next.val)
            new = ListNode(gcd)
            prev = current.next
            current.next = new
            new.next = prev
            #or new.next
            current = current.next.next
        
        return head