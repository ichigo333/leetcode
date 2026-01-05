import unittest
from solution_0019 import Solution, ListNode, get_list_length, get_list_values


class TestSolution0019(unittest.TestCase):

    def testRemovingSecondElementFromEnd(self):
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        
        solution = Solution()
        result = solution.removeNthFromEnd(head, 2)

        self.assertEqual(get_list_values(result), [1,2,3,5])
        self.assertEqual(get_list_length(result), 4)
    

    def testRemovingOnlyElement(self):
        head = ListNode(1)
        
        solution = Solution()
        result = solution.removeNthFromEnd(head, 1)

        self.assertEqual(get_list_values(result), [])
        self.assertEqual(get_list_length(result), 0)

    
    def testRemovingElementFromListWithTwoElements(self):
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        
        solution = Solution()
        result = solution.removeNthFromEnd(head, 1)

        self.assertEqual(get_list_values(result), [1])
        self.assertEqual(get_list_length(result), 1)

    
if __name__ == '__main__':
    unittest.main()