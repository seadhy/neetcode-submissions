class Solution:
    def get_frequency(self, string: str):
        frequency_map = {}

        for ch in string:
            if not ch in frequency_map:
                frequency_map[ch] = 1
            else:
                frequency_map[ch] += 1
        
        return frequency_map
    
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_frequency(s) == self.get_frequency(t)