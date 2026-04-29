class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        prevIndex, index = 0, 0
        result = [[]]

        for i in range(len(nums)):
            index = prevIndex if i >= 1 and nums[i] == nums[i-1] else 0
            prevIndex = len(result)
            for j in range(index, prevIndex):
                temp = result[j].copy()
                temp.append(nums[i])
                result.append(temp)
        
        return result