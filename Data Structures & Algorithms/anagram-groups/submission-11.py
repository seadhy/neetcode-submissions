class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_str = ''.join(x for x in sorted(s))
            if not sorted_str in anagrams:
                anagrams[sorted_str] = [s]
            else:
                anagrams[sorted_str].append(s)
        
        return list(anagrams.values())