class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)

        suffix = [1, nums[-1]]
        prefix = [1, nums[0]]

        for i in range(1, len_nums):
            prefix.append(nums[i] * prefix[i])
        
        for i in range(1, len_nums):
            suffix.append(nums[(len_nums-1) - i] * suffix[i])
        
        suffix.reverse()

        output = []
        for n in range(len(nums)):
            prefix_num = prefix[n]
            suffix_num = suffix[n+1]

            output.append(prefix_num * suffix_num)
        
        return output