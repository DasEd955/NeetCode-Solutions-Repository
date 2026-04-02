class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seenNums = [0] * len(nums)
        for num in nums:
            if seenNums[num - 1] == 1:
                return num
            seenNums[num - 1] = 1
        return -1