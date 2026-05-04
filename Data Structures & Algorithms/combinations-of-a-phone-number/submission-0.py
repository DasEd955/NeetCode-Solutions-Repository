class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        digitMap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        result, combo = list(), list()

        def dfs(index: int) -> None:
            if len(combo) == len(digits):
                result.append(''.join(combo))
                return
            
            for j in range(index, len(digits)):
                if index == len(digits):
                    return
                for value in enumerate(digitMap[digits[j]]):
                    combo.append(str(value[1]))
                    dfs(j+1)
                    combo.pop()
        
        dfs(0)
        return result