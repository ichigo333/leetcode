import unittest
from solution_2914 import Solution

class Test2914Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("1001"), 2)
        
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("10"), 1)
        
    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("0000"), 0)
        
    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.minChanges("01101110"), 3)
           
        
if __name__ == '__main__':
    unittest.main()