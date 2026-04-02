class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #mostFreq = dict()
        #result = list()

        #for num in nums:
            #if num in mostFreq:
                #mostFreq[num] += 1
            #else:
                #mostFreq[num] = 1

        #sortedFreqItems = sorted(mostFreq.items(), key=lambda item: item[1], reverse=True)
        #result = [num for num, freq in sortedFreqItems[:k]]

        #return result

        count = dict()
        frequency = [[] for i in range(len(nums) + 1)]
        result = list()

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num, count in count.items():
            frequency[count].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result    



               



