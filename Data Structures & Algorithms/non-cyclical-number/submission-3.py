class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
        return True if fast == 1 else False
    
    def sumOfSquares(self, n: int) -> int:
        result = 0
        while n != 0:
            digit = n % 10
            digit = digit ** 2
            result += digit
            n = n // 10
        return result