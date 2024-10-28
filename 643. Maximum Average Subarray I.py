class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        max_sum = windowSum

        for i in range(k,len(nums)):
            windowSum += nums[i] - nums[i-k]
            max_sum = max(windowSum,max_sum)

        return max_sum/k
  


        