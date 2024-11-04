class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        charStack = [item for item in word[::-1]]
        count = 1
        current = charStack[-1]
        
        while len(charStack) != 0:
            current = charStack.pop()
            
            if len(charStack) > 0 and current == charStack[-1] and count < 9:
                count += 1
            else:
                result.append(str(count))
                result.append(current)
                count = 1
                if len(charStack) > 0: current == charStack[-1]
        
        return "".join(result)
        

    
    
    def compressedStringFirstAttempt(self, word: str) -> str:
        result = ""
        count = 1
        current = word[0]
        
        while len(word) != 0:
            word = word[1:]
            
            if len(word) > 0 and current == word[0] and count < 9:
                count += 1
            else:
                result = "".join([result,str(count),current])
                count = 1
                if len(word) > 0: current = word[0]
                
        return result
    
    
    # official solution
    

    def compressedStringOfficial(self, word: str) -> str:
        comp = []

        # pos tracks our position in the input string
        pos = 0

        # Process until we reach end of string
        while pos < len(word):
            consecutive_count = 0

            current_char = word[pos]

            # Count consecutive occurrences (maximum 9)
            while (
                pos < len(word)
                and consecutive_count < 9
                and word[pos] == current_char
            ):
                consecutive_count += 1
                pos += 1

            # Append count followed by character to the list
            comp.append(str(consecutive_count))
            comp.append(current_char)

        # Join the list into a single string for the final result
        return "".join(comp)