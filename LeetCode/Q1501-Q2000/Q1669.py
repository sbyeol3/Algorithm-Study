# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        head = list1
        start = list1
        end = list1
        
        while end.val != b  :
            if start.val != a-1 : start = start.next
            end = end.next
        
        start.next = list2
        while start.next : start = start.next
        start.next = end.next
        
        return head