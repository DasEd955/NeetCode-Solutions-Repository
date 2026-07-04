class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        list_x = list(str_x)
        if list_x[0] == '-':
            list_x.remove('-')
            list_x.reverse()
            result = "".join(list_x)
            result =  -1 * int(result)
            if result < -2**31 or result > 2**31 - 1:
                return 0
            return result
        else:
            list_x.reverse()
            result = "".join(list_x)
            result = int(result)
            if result < -2**31 or result > 2**31 - 1:
                return 0
            return result