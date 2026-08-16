class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        anagrams = {}

        for s in strs:

            sorted_str = ''.join(x for x in sorted(s))
            if not sorted_str in seen:
                seen[sorted_str] = 1
                anagrams[sorted_str] = [s]
            else:
                seen[sorted_str] += 1
                anagrams[sorted_str].append(s)
        
        return list(anagrams.values())