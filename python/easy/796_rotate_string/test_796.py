import unittest
from solution_796 import Solution

class Test796Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.rotateString("abcde","cdeab"), True)
        
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.rotateString("abcde","abced"), False)
        
    def test_rotateString_returnFalse_ifSandGoalAreDifferentLengths(self):
        solution = Solution()
        self.assertEqual(solution.rotateString("abcde","abceddef"), False)
        
    def test_official(self):
        solution = Solution()
        self.assertEqual(solution.officialSolution("abcde","cdeab"), True)
        
    def test_officialConcatenationCheck(self):
        solution = Solution()
        self.assertEqual(solution.officialConcatenationCheck("abcde","cdeab"), True)
         
if __name__ == '__main__':
    unittest.main()