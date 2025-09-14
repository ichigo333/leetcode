from typing import List


class Solution:

    # 7ms beats 40%
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                # check that left != right for optimization?
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

    #accepted 11 ms beats 20%?
    def moveZeroes_suboptimal(self, nums: List[int]) -> None:
        length = len(nums)
        current = 0
        iteration = 0

        while iteration < length:
            if nums[current] == 0:
                del nums[current]
                nums.append(0)
                current -= 1

            current += 1
            iteration += 1
            