class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsMap = dict()
        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)
        
        for num, freq in numsMap.items():
            if freq == 1:
                return num