class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return nums

        maxArray = list()
        left, right = 0, 0
        queue = collections.deque() # stores indices

        while right < len(nums):
            # Pop smaller values from the queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            # Remove left value from the window
            if left > queue[0]:
                queue.popleft()
            if (right + 1) >= k:
                maxArray.append(nums[queue[0]])
                left += 1
            right += 1   

        return maxArray         

