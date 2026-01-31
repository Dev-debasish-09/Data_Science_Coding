class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = str(sorted(i))
            if key not in d:
                d[key] = []
            d[key].append(i)
        l = []
        for i in d:
            l.append(d[i])
        return l
        
