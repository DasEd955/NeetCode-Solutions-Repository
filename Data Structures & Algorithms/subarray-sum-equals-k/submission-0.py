class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0 : 1}
        currentPrefix, result = 0, 0

        for num in nums:
            currentPrefix += num
            needed = currentPrefix - k
            result += seen.get(needed, 0)
            seen[currentPrefix] = seen.get(currentPrefix, 0) + 1
        
        return result