class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for n in nums:
            if not n in freq_table:
                freq_table[n] = 1
            else:
                freq_table[n] += 1

        sorted_data = sorted(freq_table.items(), key=lambda x: x[1], reverse=True)[:k]
        return [x[0] for x in sorted_data]