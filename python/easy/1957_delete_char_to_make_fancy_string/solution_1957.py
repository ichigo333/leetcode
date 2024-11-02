class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        previous = ""
        found_two = False
        for x in range(0, len(s)):
            if previous != s[x]:
                result += s[x]
                previous = s[x]
                count = False
            elif previous == s[x] and count == False:
                result += s[x]
                count = True
     
        return result
    

    def betterSolution(self, s: str) -> str:
            result = []
            for c in s:
                if len(result) < 2 or not (result[-1] == c and result[-2] == c):
                    result.append(c)
            return ''.join(result)
    
# Initialize the Result: Start with an empty result string (or list in Python).
# Iterate Through Each Character:

#     For each character in the input string:
#         If the result string has fewer than two characters, add the current character without checks, since two consecutive characters can't form three in a row.
#         If there are already two characters in the result, check if the last two characters are the same as the current character:
#             If yes, skip adding this character to avoid three consecutive identical characters.
#             If no, add the character to the result.

