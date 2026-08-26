class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        stack = []
        data = {x: 0 for x in nums2}

        for i in range(len(nums2)-1, -1, -1):
            n = nums2[i]

            if not stack:
                stack.append(n)
                data[n] = -1
                continue

            while stack and n > stack[-1]:
                stack.pop()

            data[n] = -1 if not stack else stack[-1] 
            stack.append(n)

        for n in nums1:
            output.append(data[n])

        return output