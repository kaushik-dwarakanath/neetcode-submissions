class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        final_list = []
        
        for i in strs:
            key = tuple(sorted(i))
            if key not in d.keys():
                d[key] = []
            d[key].append(i)
        
        return list(d.values())