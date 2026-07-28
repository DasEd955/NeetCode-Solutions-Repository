class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDiffs = dict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seenDiffs:
                return [seenDiffs[diff], i]
            else:
                seenDiffs[num] = i