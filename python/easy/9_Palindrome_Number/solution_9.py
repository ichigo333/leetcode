class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if 0 <= x <= 9: return True
        
        if str(x) == str(x)[::-1]: return True
        
        return False
    
    def isPalindrome_SolutionOneWithoutString(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x
    
    def isPalindrome_SolutionTwoReverseHalf(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return x == reversed_num or x == reversed_num // 10