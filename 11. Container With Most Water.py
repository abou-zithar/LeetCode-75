class Solution:
    def maxArea(self, height: List[int]) -> int:
        left  = 0
        right= len(height) -1
        old_area = 0
        while left < right:
            width = right - left
            hight = min(height[right],height[left])
            new_area = hight * width
            if new_area > old_area:
                old_area = new_area

            if height[right] > height[left]:
                left +=1
            else:
                right -=1
        return old_area