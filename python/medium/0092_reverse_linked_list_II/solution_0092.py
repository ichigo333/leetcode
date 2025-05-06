# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    ## see Python DSA course sec 6 ex 20
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0: return head

        dummy = ListNode(0, head)
        previous = dummy
        
        for _ in range(left - 1):
            previous = previous.next
            
        current = previous.next
        
        for _ in range (right - left):
            move = current.next
            current.next = move.next
            move.next = previous.next
            previous.next = move
            
        return dummy.next