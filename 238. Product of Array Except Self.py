
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answers = [1] * n
        left = 1
        for i in range(n):
            answers[i]= left
            left *=nums[i]
        right =1
        for i in range(n-1,-1,-1):
            answers[i] *=right
            right *= nums[i]
        
        return answers
        
        


    
        