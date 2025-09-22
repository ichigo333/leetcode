import unittest
from solution_0345 import Solution

class Test0345Solution(unittest.TestCase):

    def test_example1(self):
        input = "IceCreAm"
        result = "AceCreIm"
        solution = Solution()

        self.assertEqual(solution.reverseVowels(input), result)

    
    def test_example2(self):
        input = "leetcode"
        result = "leotcede"
        solution = Solution()

        self.assertEqual(solution.reverseVowels(input), result)

    def test_one_letter(self):
        input = "o"
        result = "o"
        solution = Solution()

        self.assertEqual(solution.reverseVowels(input), result)

    def test_one_vowel(self):
        input = "lottttt"
        result = "lottttt"
        solution = Solution()

        self.assertEqual(solution.reverseVowels(input), result)

    def test_vowels_at_the_start(self):
        input = "aottttt"
        result = "oattttt"
        solution = Solution()

        self.assertEqual(solution.reverseVowels(input), result)