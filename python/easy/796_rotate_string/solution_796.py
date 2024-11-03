class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #if len(s) == 0 or len(goal) == 0: return False
        if len(s) != len(goal): return False
        
        for x in range(0, len(s)):
            last = s[-1:]
            s = last + s[:-1]
            if s == goal: return True
        
        return False

    #O(n2)
    def officialSolution(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        length = len(s)

        # Try all possible rotations of the string
        for _ in range(length):
            # Perform one rotation
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
    
    #O(n)
    def officialConcatenationCheck(self, s: str, goal: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(goal):
            return False

        # Create a new string by concatenating 's' with itself
        doubled_string = s + s

        # Use find to search for 'goal' in 'doubledString'
        # If find returns an index that is not -1
        # then 'goal' is a substring
        return doubled_string.find(goal) != -1