# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        result = head
        carry = 0
        while (l1 or l2 or carry):
            if l1 and l2 :
                carry = (result.val + l1.val + l2.val) // 10
                sum = result.val + l1.val + l2.val - (carry*10)
                result.val = sum
            elif l1 or l2 :
                c = l1 if l1 else l2
                carry = (result.val + c.val) // 10
                sum = result.val + c.val - (carry*10)
            elif carry :
                sum = carry
                carry = 0
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result.val = sum
            if l1 or l2 or carry :
                result.next = ListNode(carry)
            else : result.next = None
            result = result.next

        return head