class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)

        self.suffix = [1, nums[-1]]
        self.prefix = [1, nums[0]]

        for i in range(1, len_nums):
            self.prefix.append(nums[i] * self.prefix[i])
        
        for i in range(1, len_nums):
            self.suffix.append(nums[(len_nums-1) - i] * self.suffix[i])
        
        self.suffix.reverse()
        
        output = []
        for n in range(len(nums)):
            prefix_num = self.prefix[n]
            suffix_num = self.suffix[n+1]

            output.append(prefix_num * suffix_num)
        
        return output