class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for digit in digits:
            result = (result * 10) + digit
        str_list = list(str(result + 1))
        res_list = list()
        for digit in str_list:
            res_list.append(int(digit))
        return res_list