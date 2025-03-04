import unittest
from solution_0162 import Solution

class Test162Solution(unittest.TestCase):

    def test_return_index_2_when_peak_is_3(self):
        solution = Solution()
        input = [1,2,3,1]
        self.assertEqual(solution.findPeakElement(input), 2)

    def test_return_index_5_when_peak_is_5(self):
        solution = Solution()
        input = [1,2,1,3,5,6,4]
        self.assertEqual(solution.findPeakElement(input), 5)

    def test_return_index_0_when_peak_is_left_boundary(self):
        solution = Solution()
        input = [2,1]
        self.assertEqual(solution.findPeakElement(input), 0)

    def test_return_index_1_when_peak_is_right_boundary(self):
        solution = Solution()
        input = [1,2]
        self.assertEqual(solution.findPeakElement(input), 1)

    def test_return_index_0_when_there_is_one_element(self):
        solution = Solution()
        input = [1]
        self.assertEqual(solution.findPeakElement(input), 0)


if __name__ == "__main__":
    unittest.main()