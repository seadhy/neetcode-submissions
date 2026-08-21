class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > stack[-1][0]:
                print(temp, i)

                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append([temp, i])

        return result