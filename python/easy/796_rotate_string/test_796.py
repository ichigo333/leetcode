import unittest
from solution_796 import Solution

class Test796Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.rotateString("abcde","cdeab"), True)
        
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.rotateString("abcde","abced"), False)
         
if __name__ == '__main__':
    unittest.main()