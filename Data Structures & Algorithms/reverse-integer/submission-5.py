class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True if x >= 0 else False
        result, x = 0, abs(x)
        while x != 0:
            digit = x % 10
            result = (result * 10) + digit
            x = x // 10
        if result > 2**31 - 1 or result < -2**31:
            return 0 
        return result if isPositive else -result