class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sets = set(nums)
        return len(nums) != len(nums_sets)