class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for x in range(0, len(s)):
            last = s[-1]
            s = last + s[:-1]
            if s == goal: return True
        
        return False