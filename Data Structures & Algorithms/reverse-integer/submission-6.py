class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True if x >= 0 else False
        result, x = 0, abs(x)
        MAX = 2**31 - 1
        while x != 0:
            digit = x % 10
            if result > MAX // 10 or (result == MAX // 10 and digit > MAX % 10):
                return 0 
            result = (result * 10) + digit
            x = x // 10
        return result if isPositive else -result