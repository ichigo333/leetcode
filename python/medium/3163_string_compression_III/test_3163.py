import unittest
from solution_3163 import Solution

class Test3163Solution(unittest.TestCase):
    
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.compressedString("abcde"), "1a1b1c1d1e")
        
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.compressedString("aaaaaaaaaaaaaabb"), "9a5a2b")
        
    def test_word_is_1_char(self):
        solution = Solution()
        self.assertEqual(solution.compressedString("a"), "1a")
        
    def test_word_is_3a(self):
        solution = Solution()
        self.assertEqual(solution.compressedString("aaa"), "3a")
        
if __name__ == '__main__':
    unittest.main()