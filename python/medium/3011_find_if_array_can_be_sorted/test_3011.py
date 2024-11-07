import unittest
from solution_3011 import Solution

class test3011Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.canSortArray([8,4,2,30,15]), True)
    
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.canSortArray([1,2,3,4,5]), True)
    
    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.canSortArray([3,16,8,4,2]), False)
    
    def test_failed_test(self):
        solution = Solution()
        self.assertEqual(solution.canSortArray([20, 16]), False)
        
    def test_one_element(self):
        solution = Solution()
        self.assertEqual(solution.canSortArray([20]), True)



if __name__ == '__main__':
    unittest.main()