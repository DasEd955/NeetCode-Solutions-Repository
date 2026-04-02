class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                return True
            #else:
                #continue
        return False                               

                    
        