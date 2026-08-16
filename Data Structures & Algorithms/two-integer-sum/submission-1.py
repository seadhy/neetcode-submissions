class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        for i in range(nums_length):
            if i == nums_length:
                continue
            for j in range(i+1, nums_length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return [0, 0]