class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        count = dict()
        frequency = [[] for i in range(len(nums) + 1)]
        result = list()

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            frequency[freq].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result            
        