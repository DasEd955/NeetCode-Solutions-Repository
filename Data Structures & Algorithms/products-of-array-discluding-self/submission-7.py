class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #output = list()

        #for index in range(len(nums)):
            #output.append(math.prod(nums[:index]) * math.prod(nums[index+1:]))

        #return output

        output = list()
        prefix, suffix = list(), list()

        for i in range(len(nums)):
            product = math.prod(nums[:i])
            prefix.append(product)
            

        for i in reversed(range(len(nums))):
            product = math.prod(nums[i+1:])
            suffix.append(product)

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[len(nums) - 1 - i])        

        return output      
        