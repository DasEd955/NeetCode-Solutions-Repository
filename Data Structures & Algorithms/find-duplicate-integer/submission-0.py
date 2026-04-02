class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seenNums = dict()

        for num in nums:
            if num in seenNums:
                return num
            else:
                seenNums[num] = seenNums.get(num, 0)
        