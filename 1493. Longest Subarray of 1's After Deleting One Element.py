class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_counter = 0 
        left = 0 
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter +=1
                
            
            while zero_counter >  1:
                if nums[left] == 0:
                    zero_counter -=1 
                left +=1

            max_len = max(right - left ,max_len)
        return max_len
            

     