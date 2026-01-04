import unittest
from solution_0283 import Solution

class Test0283Solution(unittest.TestCase):

    def test_example1(self):
        solution = Solution()
        nums = [0]
        result = [0]
        solution.moveZeroes(nums)
        self.assertListEqual(nums, result)

    def test_example2(self):
        solution = Solution()
        nums = [0,1,0,3,12]
        result = [1,3,12,0,0]
        solution.moveZeroes(nums)
        self.assertListEqual(nums, result)

if __name__ == '__main__':
    unittest.main()