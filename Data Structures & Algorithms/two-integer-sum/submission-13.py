class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seenNums = dict()
        result = list()

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seenNums:
                return list([seenNums[diff], index])
            else:
                seenNums[num] = index    
        