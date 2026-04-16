class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        if length <= 1:
            return nums

        middle = length // 2
        leftArr, rightArr = [0] * middle, [0] * (length - middle)

        i, j = 0, 0

        for i in range(length):

            if i < middle:
                leftArr[i] = nums[i]
            else:
                rightArr[i - middle] = nums[i]
                j += 1
        
        self.sortArray(leftArr)
        self.sortArray(rightArr)
        self.merge(leftArr, rightArr, nums)
        
        return nums
    
    def merge(self, leftArr: list[int], rightArr: list[int], arr: list[int]) -> None:

        leftSize = len(arr) // 2
        rightSize = len(arr) - leftSize

        i, j, k = 0, 0, 0

        while j < leftSize and k < rightSize:

            if leftArr[j] < rightArr[k]:
                arr[i] = leftArr[j]
                i += 1
                j += 1
            else:
                arr[i] = rightArr[k]
                i += 1
                k += 1
        
        while j < leftSize:
            arr[i] = leftArr[j]
            i += 1
            j += 1
        
        while k < rightSize:
            arr[i] = rightArr[k]
            i += 1
            k += 1
        