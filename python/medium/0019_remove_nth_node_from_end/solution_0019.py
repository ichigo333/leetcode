from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
def print_head(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next
  

# LC 0019
def remove_kth_from_end(ll: LinkedList, k):     
    slow = fast = ll.head

    for _ in range(k):        
        fast = fast.next
    
    if not fast: 
        return ll.head.next  
         
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next

    return ll.head



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2

print("="*10)
print_head(remove_kth_from_end(my_linked_list, k))


print("="*10)
my_linked_list2 = LinkedList(1)
my_linked_list2.append(2)
print_head(remove_kth_from_end(my_linked_list2, k))


### Faster solution ?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0,head)
        dummy = res

        for _ in range(n):
            head=head.next

        while head:
            head=head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next
    
