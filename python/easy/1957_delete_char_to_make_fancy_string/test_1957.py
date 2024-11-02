import unittest
from solution_1957 import Solution 

class Test1957Solution(unittest.TestCase):

    def test_example1(self):
        input = "leeetcode"
        expected = "leetcode"
        solution = Solution()
        self.assertEqual(solution.makeFancyString(input), expected)


    def test_example2(self):
        input = "aaabaaaa"
        expected = "aabaa"
        solution = Solution()
        self.assertEqual(solution.makeFancyString(input), expected)

    def test_example3(self):
        input = "aab"
        expected = "aab"
        solution = Solution()
        self.assertEqual(solution.makeFancyString(input), expected)

if __name__ == '__main__':
    unittest.main()