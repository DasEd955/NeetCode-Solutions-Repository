class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        nums1Index = {num : i for i, num in enumerate(nums1)}
        stack = list()

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                result[index] = curr
            if curr in nums1Index:
                stack.append(curr)
        
        return result