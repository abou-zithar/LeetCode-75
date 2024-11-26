class Solution1:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        pivot =0 
        left_sum = 0

        while pivot < len(nums):
            if left_sum == (total_sum - left_sum - nums[pivot]):
                return pivot
            left_sum +=nums[pivot]
            pivot +=1
        return -1
            

class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        
        return -1
      
