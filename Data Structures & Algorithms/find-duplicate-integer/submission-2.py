class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seenNums = set()

        for num in nums:
            if num in seenNums:
                return num
            seenNums.add(num)
        