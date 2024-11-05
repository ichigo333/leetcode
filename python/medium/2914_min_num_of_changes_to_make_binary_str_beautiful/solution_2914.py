class Solution:
    ## best 85% runtime 70% mem
    ## matches official solution -- Greedy (optimized)
    def minChanges(self, s: str) -> int: 
        count = 0
        for index in range(0, len(s), 2):
            if s[index] != s[index + 1]:
                count += 1
        
        return count
    
    ## one line solution similar to above
    def minChangesUnofficialOneLine(self, s: str) -> int:
        return sum(s[i] != s[i+1] for i in range(0, len(s), 2))
    
    ## other attempts
    def minChangesSecondAttempt(self, s: str) -> int: ## 15%
        count = 0
        charList = [s[i:i+2] for i in range(0, len(s), 2)]
        count = sum([1 for x in charList if x[0] != x[1]])
            
        return count
    
    def minChangesFistAttempt(self, s: str) -> int: ## 15%
        count = 0
        
        for index in range(len(s)):
            if index % 2 == 0: 
                continue
            elif s[index] != s[index - 1]:
                count += 1
            
        return count