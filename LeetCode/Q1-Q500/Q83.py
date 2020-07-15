# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None : return None
        before = head.val
        newList = ListNode(before)
        answer = newList
        p = head.next
        while p :
            if p.val == before : p = p.next
            else :
                before = p.val
                newList.next = ListNode(p.val)
                newList = newList.next
                p = p.next
        return answer