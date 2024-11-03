import unittest
from solution_9 import Solution

class Test9Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(121), True)
        
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(-121), False)
        
    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(10), False)
        
    def test_IsPalindrome_ReturnsTrue_IfNumberIs0(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(0), True)
        
    def test_IsPalindrome_ReturnsTrue_IfNumberIs9(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(0), True)
        
    def test_example1_solutionOneWithoutString(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome_SolutionOneWithoutString(121), True)
    
    def test_example1_solutionTwoReversingHalf(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome_SolutionTwoReverseHalf(1221), True)
        
if __name__ == '__main__':
    unittest.main()