class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        output = []
        stack = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]

            while stack and h > stack[-1]:
                stack.pop()

            if not stack:
                output.append(i)

            stack.append(h)

        return output[::-1]