from typing import Optional


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))
            
    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return self
        
        previous = Node(-1, self.head)
        current = self.head
        dummy: Node = previous
        
        while current:
            is_dupe: bool = False
            
            while current.next and current.value == current.next.value:
                is_dupe = True
                current = current.next
            
            if is_dupe:
                previous.next = current.next
            else:
                previous = previous.next
            
            current = current.next
            
        self.head = dummy.next
            


#### TESTS #####

def test_remove_duplicates(linked_list, expected_values):
    print("Before: ", end="")
    linked_list.print_list()
    linked_list.remove_duplicates()
    print("After:  ", end="")
    linked_list.print_list()

    # Collect values from linked list after removal
    result_values = []
    node = linked_list.head
    while node:
        result_values.append(node.value)
        node = node.next

    # Determine if the test passes
    if result_values == expected_values:
        print("Test PASS\n")
    else:
        print("Test FAIL\n")
        
# Test 1

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(5)
test_remove_duplicates(ll, [1, 2, 5])


# Test 2

ll = LinkedList(1)
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [2, 3])


# Test 3

ll = LinkedList(1)
ll.append(1)
ll.append(2)
ll.append(3)
test_remove_duplicates(ll, [2, 3])



### solution adapted to LC

#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        previous = ListNode(-1, head)
        current = head
        dummy = previous
        
        while current:
            is_dupe: bool = False
            
            while current.next and current.val == current.next.val:
                is_dupe = True
                current = current.next
            
            if is_dupe:
                previous.next = current.next
            else:
                previous = previous.next
            
            current = current.next
            
        return dummy.next