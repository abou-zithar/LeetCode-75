class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_counter = 0
        
        for right in range(len(nums)):
            # If we encounter a 0, increase the zero counter
            if nums[right] == 0:
                zero_counter += 1
            
            # If zero_counter exceeds k, move the left pointer
            # to keep the window valid
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
            
            # Calculate the current length and update max_len
            max_len = max(max_len, right - left + 1)
        
        return max_len
            
        