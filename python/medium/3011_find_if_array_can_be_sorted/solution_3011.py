class Solution:
    # accepted
    # 8ms 65% runtime 79% on memory
    def canSortArray(self, nums) -> bool:
        final_list = self.getSortedLists(nums)
        if len(final_list) == 1: return True
        
        for index in range(len(final_list)):
            if index == len(final_list) - 1: continue
            if max(final_list[index]) > min(final_list[index + 1]):
                return False
        
        return True

    def getSortedLists(self, nums):
        curr_set_bit_number = 0
        temp_list = []
        final_list = []
        for index in range(len(nums)):
            temp_bit = nums[index].bit_count()
            if len(temp_list) == 0:
                curr_set_bit_number = temp_bit
                temp_list.append(nums[index])
            elif temp_bit == curr_set_bit_number:
                temp_list.append(nums[index])
            else:
                final_list.append(temp_list.copy())
                temp_list.clear()
                temp_list.append(nums[index])
                curr_set_bit_number = temp_bit
        
        final_list.append(temp_list.copy())
        return final_list
    
    #### Official solutions ####
    # two loops O(n^2)
    def canSortArrayTwoLoops(self, nums):
        n = len(nums)

        # Avoid modifying the input directly
        # Create a copy of the input array
        values = nums.copy()

        for i in range(n):
            for j in range(n - i - 1):
                if values[j] <= values[j + 1]:
                    # No swap needed
                    continue
                else:
                    if bin(values[j]).count("1") == bin(values[j + 1]).count(
                        "1"
                    ):
                        # Swap the elements
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True
    
    # segment solution
    # O(n)
    
    def canSortArraySortableSegment(self, nums):
        # Number of set bits of the elements in the current segment
        num_of_set_bits = bin(nums[0]).count("1")
        max_of_segment = nums[0]
        min_of_segment = nums[0]

        # Initialize max of the previous segment to the smallest possible integer
        max_of_prev_segment = float("-inf")

        for i in range(1, len(nums)):
            if bin(nums[i]).count("1") == num_of_set_bits:
                # Element belongs to the same segment
                # Update min and max values of the segment
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])
            else:  # Element belongs to a new segment
                # Check if the segments are arranged properly
                if min_of_segment < max_of_prev_segment:
                    return False

                # Update the previous segment's max
                max_of_prev_segment = max_of_segment

                # Start a new segment with the current element
                max_of_segment = nums[i]
                min_of_segment = nums[i]
                num_of_set_bits = bin(nums[i]).count("1")

        # Final check for proper segment arrangement
        if min_of_segment < max_of_prev_segment:
            return False

        return True