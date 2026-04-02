class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDiffs = dict()
        for i, value in enumerate(nums):
            diff = target - nums[i]          
            if diff in seenDiffs:
                return [seenDiffs[diff], i]
            else:
                seenDiffs[value] = i   