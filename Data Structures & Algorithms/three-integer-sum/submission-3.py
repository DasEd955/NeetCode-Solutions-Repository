class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum > 0:
                    k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1    
        return result                             
        