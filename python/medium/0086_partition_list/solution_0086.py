# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None

        low_head = ListNode()
        high_head = ListNode()
        tail_low = low_head
        tail_high = high_head
        current = head

        while current:
            if current.val < x:
                tail_low.next = current
                tail_low = tail_low.next
            else:
                tail_high.next = current
                tail_high = tail_high.next
            
            current = current.next

        tail_low.next = high_head.next
        tail_high.next = None
        return low_head.next
    



def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


#[1,4,3,2,5,2]
test1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print(f"before  : {linked_list_to_list(test1)}")
print(f"expected: [1, 2, 2, 4, 3, 5]")
result = Solution()
print(f"result  : {linked_list_to_list(result.partition(test1, 3))}")