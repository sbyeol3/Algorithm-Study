# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head : return False
        node = head
        visitied = set()
        while node :
            if node in visitied : return True
            visitied.add(node)
            node = node.next
            
        return False