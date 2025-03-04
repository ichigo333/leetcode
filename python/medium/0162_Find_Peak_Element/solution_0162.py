from typing import List


class Solution:
    
    def findPeakElement_BigOnSolution(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        max_num = max(nums)
        return nums.index(max_num)
    
    def findPeakElement_cutting_solution(self, nums: List[int]) -> int:
        sub_list = nums.copy()

        while True:
            length = len(sub_list)
            if length == 1:
                return nums.index(sub_list[0])
            
            if length == 2:
                return nums.index(sub_list[0]) if sub_list[0] > sub_list[1] else nums.index(sub_list[1])

            middle = (length-1) // 2
            if sub_list[middle-1] > sub_list[middle+1]:
                sub_list = sub_list[0:middle+1]
            else:
                sub_list = sub_list[middle:length]
        

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[middle + 1]:
                right = middle
            else:
                left = middle + 1

        return left
    


solution = Solution()
input = [1,2,3,1]
print(solution.findPeakElement(input))