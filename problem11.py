class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right, h = 0, len(height) - 1, 0
        max_area = 0
        while right > left:
            w = right - left
            if height[left] > height[right]:
                h = height[right]
                right = right - 1
            else:
                h = height[left]
                left = left + 1
                
            max_area = max(max_area, h * w)
        
        
        return max_area

   
