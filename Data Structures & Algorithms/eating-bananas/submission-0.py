class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)

        while low <= high:
            middle = low + (high - low) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/middle)
            if totalHours <= h:
                high = middle - 1
            else:
                low = middle + 1
        
        return low