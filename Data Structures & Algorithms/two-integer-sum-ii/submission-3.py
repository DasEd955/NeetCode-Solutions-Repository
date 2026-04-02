class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                result.append(left+1)
                result.append(right+1)
                right -= 1
                left += 1
        return result        


            
        