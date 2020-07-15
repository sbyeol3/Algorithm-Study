# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryStr, decimalValue = '', 0
        while(head) :
            binaryStr += str(head.val)
            head = head.next
        for b in range(len(binaryStr)) :
            val = int(binaryStr[b])
            power = len(binaryStr) - b - 1
            decimalValue += val * (2 ** power)
        return decimalValue