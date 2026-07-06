class Solution:
    def isHappy(self, n: int) -> bool:
        seenSums = set()
        curSum = 0
        while curSum != 1:
            curSum = 0
            while n != 0:
                digit = n % 10
                curSum += digit ** 2
                n = n // 10
            if curSum in seenSums:
                return False
            seenSums.add(curSum)
            if curSum != 1:
                n = curSum
        return True
            
            