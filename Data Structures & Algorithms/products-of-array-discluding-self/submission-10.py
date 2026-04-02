class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #output = list()

        #for index in range(len(nums)):
            #output.append(math.prod(nums[:index]) * math.prod(nums[index+1:]))

        #return output

        n = len(nums)
        output = list()
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]          

        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(0,n):
            output.append(prefix[i] * suffix[i]) 

        return output      
        