class Solution:
    def __init__(self):
        self.stack = []
        self.max_area = 0

    def updateMaxArea(self, area) -> None:
        if area > self.max_area:
            self.max_area = area

    def calculateAreas(self, total_len) -> None:
        while self.stack:
            index, h = self.stack.pop()
            self.updateMaxArea(h * (total_len - index))

    def largestRectangleArea(self, heights: List[int]) -> int:
        self.stack = []
        self.max_area = 0
        for i in range(len(heights)):
            h = heights[i]
            if not self.stack:
                self.stack.append([i, h])
            else:
                last_popped_index = i
                while self.stack and h < self.stack[-1][1]:
                    last_popped_index, last_popped_height = self.stack.pop()
                    self.updateMaxArea(last_popped_height * (i - last_popped_index))

                self.stack.append([last_popped_index, h])

        self.calculateAreas(len(heights))
        return self.max_area