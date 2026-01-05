import unittest
from solution_0004 import Solution

class TestSolution0004(unittest.TestCase):

    def testOddNumberOfElements(self):
        nums1 = [1,3]
        nums2 = [2]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.0)


    def testEvenNumberOfElements(self):
        nums1 = [1,2]
        nums2 = [3,4]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)

    
    def testLargerArrays(self):
        nums1 = [1,2,5,6,9]
        nums2 = [3,4,6,7]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 5)


    def testArrayIsEmpty(self):
        nums1 = []
        nums2 = [3,4,6,7]

        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()