class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = dict()
        result = list()

        for num in nums:
            if num in mostFreq:
                mostFreq[num] += 1
            else:
                mostFreq[num] = 1

        sortedFreqItems = sorted(mostFreq.items(), key=lambda item: item[1], reverse=True)
        
        return [num for num, freq in sortedFreqItems[0:k]]