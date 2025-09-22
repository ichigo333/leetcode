class Solution:

    # 15ms better than 39%
    def reverseVowels_FirstAttempt(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = list(s)

        left_index = 0
        right_index = len(s)-1
        left = False
        right = False

        while left_index < right_index:
            if word[left_index].lower() not in vowels:
                left_index += 1
            else:
                left = True

            if word[right_index].lower() not in vowels:
                right_index -= 1
            else:
                right = True
            
            if left and right:
                word[left_index], word[right_index] = word[right_index], word[left_index]
                left, right = False, False
                left_index += 1
                right_index -= 1

        return "".join(word)

    # simplified but somehow worse 17ms
    def reverseVowels_simplified(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = list(s)

        left_index = 0
        right_index = len(s)-1

        while left_index < right_index:
            if word[left_index].lower() not in vowels:
                left_index += 1
            elif word[right_index].lower() not in vowels:
                right_index -= 1
            else:
                word[left_index], word[right_index] = word[right_index], word[left_index]
                left_index += 1
                right_index -= 1

        return "".join(word)
    
    # best solution 3ms, because moving each pointer and not moving outer loop
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

solution = Solution()
result = solution.reverseVowels("hello")
print(result)