class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for digit in digits:
            result = (result * 10) + digit
        return list(str(result + 1))