class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        duplicate = nums.copy()
        for num in duplicate:
            nums.append(num)
        
        return nums