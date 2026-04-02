class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seenDiffs = dict()
        result = list()

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seenDiffs:
                return [seenDiffs[diff], index]
            else:
                seenDiffs[num] = index    
        