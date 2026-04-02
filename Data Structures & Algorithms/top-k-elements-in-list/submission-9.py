class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = dict()

        for num in nums:
            if num in mostFreq:
                mostFreq[num] += 1
            else:
                mostFreq[num] = 1

        sortedMostFreq = sorted(mostFreq.items(), key = lambda item: item[1], reverse=True)

        #for mostFreq.values() >= k:
        return [key for key, _ in sortedMostFreq[:k]]            

        #mostFreq = dict()
        #result = list()

        #for num in nums:
            #if num in mostFreq:
                #mostFreq[num] += 1
            #else:
                #mostFreq[num] = 1

        #if k > 1:
            #result.append(mostFreq[num])
            #result.append(mostFreq[k])
        #else:
            #return [key for key, value in mostFreq.items()]

        #return result        

        