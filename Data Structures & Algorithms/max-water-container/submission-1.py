class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # lets do the brute force first
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            container_height = min(heights[right], heights[left])

            area = width * container_height
            max_area = max(max_area, area)

            # pointer moving
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


            

