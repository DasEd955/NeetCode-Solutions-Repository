class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seenNums = dict()

        for num in nums:
            seenNums[num] = 1 + seenNums.get(num, 0)
        
        inverted_dict = {v: k for k, v in seenNums.items()}
        key = inverted_dict.get(max(seenNums.values()))

        return key
        