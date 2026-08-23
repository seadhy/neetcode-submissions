class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            popped_i = i
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                max_area = max(max_area, popped_h * (i - popped_i))

            stack.append([popped_i, h])

        for bar in stack:
            h = min(stack[-1][1], bar[1])
            w = len(heights) - bar[0]
            max_area = max(max_area, h * w)
            
        return max_area